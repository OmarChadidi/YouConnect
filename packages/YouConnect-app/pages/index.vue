<script setup lang="ts">
import { PrimaryButton, TertiaryButton } from "@youcan/ui-vue3";
import Profile from "~/components/Profile.vue";

let pages = [
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
// pages = [];
</script>

<template>
  <div>
    <section class="flex justify-between items-center">
      <header>
        <h1 class="text-lg font-bold">YouCan Connect</h1>
        <h2>Select a page to continue</h2>
      </header>

      <div v-if="pages.length > 0" class="flex gap-4">
        <NuxtLink to="/profiles/create">
          <PrimaryButton icon-position="left">
            <template #icon>
              <i class="i-youcan:plus"></i>
            </template>
            Create profile
          </PrimaryButton>
        </NuxtLink>
      </div>
    </section>

    <section class="mt-6 space-y-6">
      <div class="flex flex-col justify-center relative">
        <template v-if="pages.length === 0">
          <div
            class="bg-zinc-100 border h-[340px] rounded flex flex-col items-center justify-center"
          >
            <svg
              width="62"
              height="62"
              viewBox="0 0 62 62"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <rect
                width="62"
                height="62"
                rx="31"
                fill="url(#paint0_linear_18_1564)"
              />
              <path
                d="M23.1687 38.4162L20.8197 38.4162C18.7038 38.399 16.6805 37.5464 15.1904 36.0441C13.7003 34.5418 12.8641 32.5115 12.8641 30.3956C12.8641 28.2796 13.7003 26.2494 15.1904 24.7471C16.6805 23.2448 18.7038 22.3922 20.8197 22.375L26.5114 22.3809C28.5572 22.3788 30.5265 23.1585 32.0163 24.5605C33.5062 25.9625 34.404 27.8808 34.5261 29.923"
                stroke="black"
                stroke-width="4.42857"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M37.376 22.375L39.725 22.375C41.8409 22.3922 43.8643 23.2449 45.3544 24.7471C46.8445 26.2494 47.6806 28.2797 47.6806 30.3956C47.6806 32.5116 46.8445 34.5418 45.3544 36.0441C43.8642 37.5464 41.8409 38.399 39.725 38.4163L34.0274 38.4163C31.9816 38.4167 30.013 37.6355 28.5243 36.2324C27.0356 34.8294 26.1392 32.9104 26.0186 30.8683"
                stroke="black"
                stroke-width="4.42857"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <defs>
                <linearGradient
                  id="paint0_linear_18_1564"
                  x1="31"
                  y1="0"
                  x2="31"
                  y2="77.5"
                  gradientUnits="userSpaceOnUse"
                >
                  <stop stop-color="#FF91E7" />
                  <stop offset="0.485" stop-color="#FDD0F3" />
                  <stop offset="1" stop-color="#FF9EEA" />
                </linearGradient>
              </defs>
            </svg>

            <p class="p-4 text-center">Currently you don’t have any link</p>
            <div class="flex gap-4">
              <NuxtLink to="/profiles/create">
                <PrimaryButton icon-position="left">
                  <template #icon>
                    <i class="i-youcan:plus"></i>
                  </template>
                  Create profile
                </PrimaryButton>
              </NuxtLink>
            </div>
          </div>
        </template>
        <Profile
          v-else
          v-for="page in pages"
          :key="page.title"
          :title="page.title"
          :url="page.url"
        />
      </div>
    </section>
  </div>
</template>
