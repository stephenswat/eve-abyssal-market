<script setup lang="ts">
defineProps(['title'])
</script>

<template>
  <div class="container-fluid d-flex flex-column ng-scope">
    <div class="row align-items-center bg-primary check-contrast py-5">
      <div class="col-xl-9 container-alt text-light toggles-ignore mx-auto text-lg-left">
        <h1 class="display-3 mb-0">
          <span
            data-ng-bind="selected.palette.name"
            class="ng-binding"
          >{{ title }}</span>
        </h1>
        <p class="lead mb-3">
          <span
            data-ng-bind="selected.palette.desc"
            class="ng-binding"
          ><slot /></span>
        </p>
      </div>
    </div>
  </div>
</template>
