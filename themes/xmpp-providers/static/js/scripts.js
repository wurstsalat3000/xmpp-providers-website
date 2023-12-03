// SPDX-FileCopyrightText: 2022 XMPP Providers Team
//
// SPDX-License-Identifier: AGPL-3.0-or-later

document.addEventListener("DOMContentLoaded", (event) => {
  // Initialize Bootstrap tooltips
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

  initialize_provider_filters()
  initialize_copy_badge_button()
  initialize_contact_page_clients()
});

function initialize_provider_filters() {
  // Provider filtering in overview
  const checkboxes = document.querySelectorAll("#status-selector input");
  const show_hide = function(checkbox) {
    const property = checkbox.getAttribute("name");
    if (property == "free") {
      const relevant_providers = document.querySelectorAll("[data-property-free=false]");
      relevant_providers.forEach(function(provider) {
        provider.hidden = checkbox.checked;
      });
    };
    if (property == "professional-hosting") {
      const relevant_providers = document.querySelectorAll("[data-property-professional-hosting=false]");
      relevant_providers.forEach(function(provider) {
        provider.hidden = checkbox.checked;
      });
    };
    if (property == "rating-green-web-check") {
      const relevant_providers = document.querySelectorAll("[data-property-rating-green-web-check=false]");
      relevant_providers.forEach(function(provider) {
        provider.hidden = checkbox.checked;
      });
    };
    if (property == "in-band-registration") {
      const relevant_providers = document.querySelectorAll("[data-property-ibr=false]");
      relevant_providers.forEach(function(provider) {
        provider.hidden = checkbox.checked;
      });
    };
    if (property == "password-reset") {
      const relevant_providers = document.querySelectorAll("[data-property-password-reset=false]");
      relevant_providers.forEach(function(provider) {
        provider.hidden = checkbox.checked;
      });
    };
    checkbox.addEventListener("click", function(event) {
      show_hide(event.target);
    });
  };
  checkboxes.forEach(show_hide);
}

function initialize_copy_badge_button() {
  // Copy badge embed link to clipboard
  const badge_link_copy = document.getElementById("badge_link_copy");
  if (badge_link_copy) {
    badge_link_copy.addEventListener("click", function() {
      navigator.clipboard.writeText(document.getElementById("badge_link_input").value);

      // Notifications
      const copy_toast = document.getElementById("copy_toast")
      const toast_alert = bootstrap.Toast.getOrCreateInstance(copy_toast)
      toast_alert.show()
      const tooltip = bootstrap.Tooltip.getInstance("#badge_link_copy")
      tooltip.hide()
    });
  }
}

function initialize_contact_page_clients() {
  // Recommended clients list filtering on /contact page
  const recommended_clients_list = document.getElementById("recommended_clients_list");
  if (recommended_clients_list) {
    const filter_clients = function(os_name) {
      for (const client of recommended_clients_list.children) {
        client.hidden = os_name != client.getAttribute("data-os");
      };
    };
    if (navigator.userAgent.indexOf("Android") >= 0) {
      filter_clients("Android");
    } else if (navigator.userAgent.indexOf("Linux") >= 0)  {
      filter_clients("Linux");
    } else if (navigator.userAgent.indexOf("iPhone") >= 0)  {
      filter_clients("iPhone");
    } else {
      filter_clients("Windows");
    }
  }
}