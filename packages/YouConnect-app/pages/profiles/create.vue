<script setup lang="ts">
import { DropdownPrefix, InputGroup, PrimaryButton, TertiaryButton, TextArea } from "@youcan/ui-vue3";

const slug = ref("");
const name = ref("");
const description = ref("");

const urls = [{ label: 'https://youcanconnect.com/' }];

const isLoading = ref(false);

const handleCreateProfile = () => {
  isLoading.value = true;

  console.log('Creating profile', slug.value, name.value, description.value);

  isLoading.value = false;
};
</script>

<template>
  <div>
    <header class="flex gap-4 items-center">
      <NuxtLink to="/">
        <TertiaryButton>
          <i class="i-youcan:caret-left"></i>
        </TertiaryButton>
      </NuxtLink>
      <h2 class="text-xl font-semibold">Create profile</h2>
    </header>

    <form class="mt-6 border rounded-lg p-4" @submit.prevent="handleCreateProfile">
      <h3 class="text-lg mb-6">Profile info</h3>

      <div class="space-y-3">
        <InputGroup>
          <template #label>
            Slug
          </template>

          <template #input>
            <Input v-model="slug" placeholder="Enter slug">
              <template #prefix>
                <DropdownPrefix type="button" :items="urls" :placeholder="urls[0].label"/>
              </template>
            </Input>
          </template>
        </InputGroup>

        <InputGroup>
          <template #label>
            Name
          </template>

          <template #input>
            <Input v-model="name" placeholder="Your profile name"/>
          </template>
        </InputGroup>

        <InputGroup>
          <template #label>
            Description
          </template>

          <template #input>
            <TextArea v-model="description" placeholder="Your profile description"/>
          </template>
        </InputGroup>

        <div class="flex justify-end">
          <PrimaryButton icon-position="left" :disabled="isLoading">
            <template #icon>
              <i class="i-youcan:plus"></i>
            </template>
            Create profile
          </PrimaryButton>
        </div>
      </div>
    </form>
  </div>
</template>
