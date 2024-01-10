<script setup lang="ts">
</script>

<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-primary fixed-top">
    <div class="container-fluid">
      <router-link
        to="/"
        class="navbar-brand"
      >
        mutaplasmid.space
      </router-link>

      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar-toggled"
      >
        <span class="navbar-toggler-icon" />
      </button>

      <div
        id="navbar-toggled"
        class="collapse navbar-collapse"
      >
        <ul class="navbar-nav navbar-fill">
          <li
            class="nav-item dropdown dropdown-accordion"
            data-accordion="#module-accordion"
          >
            <a
              id="navbarDropdown"
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              data-bs-auto-close="outside"
            >
              Modules
            </a>
            <div class="dropdown-menu module-dropdown">
              <div class="row mx-2 my-2">
                {% get_abyssal_type_list as type_list %}
                {% for r, l in type_list %}
                <span class="col-md-3 col-12 align-middle">
                  <img
                    height="21px"
                    src="https://image.eveonline.com/Type/{{ l.0.1 }}_32.png"
                    style="padding-right: 7px;"
                  >{{ r }}
                </span>
                <div class="col-md-9 col-12 row m-0 p-0">
                  {% for n, i in l %}
                  <span class="col p-1"><a
                    class="btn btn-sm btn-primary btn-block py-0"
                    style="font-size: small;"
                    href="{% url 'abyssal_modules:type_module_list' i %}"
                  >{{ n }}</a></span>
                  {% endfor %}
                </div>
                <div class="w-100" />
                {% endfor %}
              </div>
            </div>
          </li>
          <li class="nav-item">
            <router-link
              to="/appraisal"
              class="nav-link"
            >
              Appraisal
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              to="/support"
              class="nav-link"
            >
              Support Us
            </router-link>
          </li>
          <li class="nav-item">
            <a
              class="nav-link"
              href="http://discord.gg/sFrvsGg"
            >Discord</a>
          </li>
        </ul>
        <ul class="navbar-nav navbar-right">
          <li class="nav-item mr-3">
            <a
              class="nav-link"
              href="javascript:toggle_mode()"
            >
              <i
                id="mode-toggle"
                class="fa fa-moon-o"
                aria-hidden="true"
              />
              <span class="d-md-none">Dark/light mode</span>
            </a>
          </li>
          <!-- {% if user.is_authenticated %}
        <li class="nav-item dropdown my-auto mr-3">
          <a class="nav-link dropdown-toggle py-0 mr-2" href="#" id="navbar_character_dropdown" role="button" data-toggle="dropdown">
            <img src="https://image.eveonline.com/Character/1_32.jpg" height="32px" class="avatar mr-0" id="current_character_avatar"/>
            <span class="align-middle" id="current_character_name"></span>
          </a>
          <div class="dropdown-menu" id="character_select_list">
          </div>
        </li>
        <li class="nav-item my-auto mr-3">
          <a class="nav-link p-0" href="{% url 'eve_auth:profile' %}">
            <i class="fas fa-user mr-1"></i> Account
          </a>
        </li>
        <li class="nav-item my-auto mr-3">
          <a class="nav-link" href="{% url 'eve_auth:logout' %}">
            <i class="fas fa-sign-out-alt mr-1"></i> Log out
          </a>
        </li>
      {% else %}
        <li class="nav-item my-auto mr-3">
          <a class="nav-link" href="{% url 'eve_auth:login' %}">
            <i class="fas fa-sign-in-alt mr-1"></i> Log in
          </a>
        </li>
      {% endif %} -->
        </ul>
      </div>
    </div>
  </nav>

  <div
    class="container"
    style="min-height: 56px;"
  />

  <router-view />

  <div
    class="container"
    style="min-height: 56px;"
  />

  <div class="container">
    <footer class="mt-auto py-3 text-light">
      Made with &#x1F914;&#x1F52A; by <a href="https://evewho.com/pilot/Sharad+Heft">Sharad Heft</a> &bull;
      <router-link to="/faq">
        FAQ
      </router-link> &bull;
      <router-link to="/legal">
        Legal
      </router-link> &bull;
      <router-link to="/statistics">
        Statistics
      </router-link> &bull;
      <a href="https://github.com/StephenSwat/eve-abyssal-market">GitHub</a>
    </footer>
  </div>

<!-- {{ eve_characters|json_script:'eve_characters' }} -->
</template>

<style scoped>
</style>
