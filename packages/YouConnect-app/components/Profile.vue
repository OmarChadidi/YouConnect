<script lang="ts" setup>
defineProps<{
  title: string;
  url: string;
}>();
</script>

<template>
  <a
    :href="url"
    class="group flex justify-between items-center bg-white hover:bg-gray-50 p-3 rounded-lg mx-3 my-3 shadow-md border"
  >
    <div class="flex gap-6 items-center">
      <div class="group-hover:bg-gray-200 p-2 rounded-full">
        <i class="i-youcan:storefront"></i>
      </div>

      <div>
        <p class="text-lg font-semibold">
          {{ title }}
        </p>
        <p>
          {{ url }}
        </p>
      </div>
    </div>

    <i class="i-youcan:caret-right"></i>
  </a>
</template>
