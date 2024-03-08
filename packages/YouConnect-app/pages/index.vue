<script setup lang="ts">
import { PrimaryButton, TertiaryButton } from "@youcan/ui-vue3";
import Profile from "~/components/Profile.vue";

const pages = [
  {
    title: "My First profiles",
    url: "https://youcanconnect.com/my-first-page",
  },
  {
    title: "My Second profiles",
    url: "https://youcanconnect.com/my-second-page",
  },
  {
    title: "My Third profiles",
    url: "https://youcanconnect.com/my-third-page",
  },
];
</script>

<template>
  <div class="max-w-2xl mx-auto my-4">
    <section class="flex justify-between items-center">
      <header>
        <h1 class="text-lg font-bold">YouCan Connect</h1>
        <h2>Select a page to continue</h2>
      </header>

      <div class="flex gap-4">
        <NuxtLink to="/profiles/create">
          <PrimaryButton icon-position="left">
            <template #icon>
              <i class="i-youcan:plus"></i>
            </template>
            Create
          </PrimaryButton>
        </NuxtLink>
      </div>
    </section>

    <section class="mt-6 space-y-6">
      <Profile v-for="page in pages" :key="page.title" :title="page.title" :url="page.url"/>
    </section>
  </div>
</template>
