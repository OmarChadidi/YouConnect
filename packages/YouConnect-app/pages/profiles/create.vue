<script setup lang="ts">
import { TertiaryButton } from "@youcan/ui-vue3";
</script>

<template>
  <div class="max-w-4xl mx-auto my-4">
    <header class="flex gap-4 items-center">
      <NuxtLink to="/">
        <TertiaryButton>
          <i class="i-youcan:caret-left"></i>
        </TertiaryButton>
      </NuxtLink>
      <h2 class="text-xl font-semibold">Create profile</h2>
    </header>

    <section class="flex justify-between items-center mt-6">
      TEST
    </section>
  </div>
</template>
