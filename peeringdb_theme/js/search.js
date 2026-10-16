/*
 * Site search for peeringdb_theme, backed by the search index Zensical
 * builds (search.json: {config, items: [{location, title, text, ...}]}).
 *
 * Zensical's own search UI ships inside its Material-style theme, which this
 * standalone theme does not load, so this script reads the index directly and
 * renders into the MkDocs-style search modal. The index format is not a
 * documented contract: if it changes, the modal reports search as unavailable
 * rather than breaking the page.
 */
(function () {
  var MIN_QUERY_LENGTH = 3;
  var MAX_RESULTS = 50;
  var SUMMARY_LENGTH = 200;

  var index = null;
  var failed = false;
  var separator = /[\s\-_,:!=\[\]()\\"`/]+|\.(?!\d)/;

  function joinUrl(base, path) {
    if (path.charAt(0) === "/") {
      return path;
    }
    if (base.charAt(base.length - 1) === "/") {
      return base + path;
    }
    return base + "/" + path;
  }

  function escapeHtml(value) {
    return value.replace(/&/g, "&amp;")
      .replace(/"/g, "&quot;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function stripTags(html) {
    var el = document.createElement("div");
    el.innerHTML = html;
    return (el.textContent || "").replace(/\s+/g, " ").trim();
  }

  function getSearchTermFromLocation() {
    var params = window.location.search.substring(1).split("&");
    for (var i = 0; i < params.length; i++) {
      var pair = params[i].split("=");
      if (pair[0] === "q" && pair[1]) {
        return decodeURIComponent(pair[1].replace(/\+/g, "%20"));
      }
    }
  }

  function loadIndex(data) {
    if (!data || !Array.isArray(data.items)) {
      throw new Error("unexpected search.json format");
    }
    if (data.config && data.config.separator) {
      try {
        separator = new RegExp(data.config.separator);
      } catch (e) { /* keep default */ }
    }
    index = [];
    data.items.forEach(function (item) {
      if (typeof item.location !== "string" || typeof item.title !== "string") {
        return;
      }
      var text = stripTags(item.text || "");
      index.push({
        location: item.location,
        title: item.title,
        titleLower: item.title.toLowerCase(),
        text: text,
        textLower: text.toLowerCase(),
        level: item.level || 1
      });
    });
  }

  function tokenize(query) {
    return query.toLowerCase().split(separator).filter(function (t) {
      return t.length > 0;
    });
  }

  function search(query) {
    var terms = tokenize(query);
    if (!terms.length) {
      return [];
    }
    var results = [];
    index.forEach(function (doc) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var inTitle = doc.titleLower.indexOf(terms[i]) !== -1;
        var inText = doc.textLower.indexOf(terms[i]) !== -1;
        if (!inTitle && !inText) {
          return;
        }
        score += (inTitle ? 10 : 0) + (inText ? 1 : 0);
      }
      if (doc.level === 1) {
        score += 1;
      }
      results.push({doc: doc, score: score});
    });
    results.sort(function (a, b) { return b.score - a.score; });
    return results.slice(0, MAX_RESULTS).map(function (r) { return r.doc; });
  }

  function formatResult(doc) {
    var summary = doc.text.length > SUMMARY_LENGTH
      ? doc.text.substring(0, SUMMARY_LENGTH) + "…"
      : doc.text;
    return '<article><h3><a href="' + joinUrl(base_url, doc.location) + '">' +
      escapeHtml(doc.title) + "</a></h3><p>" + escapeHtml(summary) + "</p></article>";
  }

  function display(html) {
    var container = document.getElementById("mkdocs-search-results");
    container.innerHTML = html;
  }

  function displayResults(results) {
    if (results.length) {
      display(results.map(formatResult).join(""));
    } else {
      var container = document.getElementById("mkdocs-search-results");
      var text = container.getAttribute("data-no-results-text") || "No results found";
      display("<p>" + escapeHtml(text) + "</p>");
    }
  }

  function doSearch() {
    var query = document.getElementById("mkdocs-search-query").value;
    if (failed) {
      display("<p>Search is currently unavailable.</p>");
    } else if (!index) {
      display("");
    } else if (query.length >= MIN_QUERY_LENGTH) {
      displayResults(search(query));
    } else {
      display("");
    }
  }

  function init() {
    var input = document.getElementById("mkdocs-search-query");
    if (!input) {
      return;
    }
    input.addEventListener("keyup", doSearch);
    fetch(joinUrl(base_url, "search.json"))
      .then(function (response) {
        if (!response.ok) {
          throw new Error("HTTP " + response.status);
        }
        return response.json();
      })
      .then(loadIndex)
      .catch(function (err) {
        failed = true;
        console.warn("Search index could not be loaded:", err);
      })
      .then(function () {
        var term = getSearchTermFromLocation();
        if (term) {
          input.value = term;
        }
        if (input.value) {
          doSearch();
        }
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
