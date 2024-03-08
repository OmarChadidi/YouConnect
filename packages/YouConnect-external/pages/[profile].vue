<script lang="ts" setup>
const productList = [
  {
    image:
      "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    brand: "Brand 1",
    name: "Product Name 1",
    price: "$149",
    discounted_price: "$199",
    add_to_cart_icon: "bi bi-bag-plus",
  },
  {
    image:
      "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    brand: "Brand 2",
    name: "Product Name 2",
    price: "$149",
    discounted_price: "$199",
    add_to_cart_icon: "bi bi-bag-plus",
  },
  {
    image:
      "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    brand: "Brand 3",
    name: "Product Name 3",
    price: "$149",
    discounted_price: "$199",
    add_to_cart_icon: "bi bi-bag-plus",
  },
  {
    image:
      "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    brand: "Brand 4",
    name: "Product Name 4",
    price: "$149",
    discounted_price: "$199",
    add_to_cart_icon: "bi bi-bag-plus",
  },
  {
    image:
      "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    brand: "Brand 5",
    name: "Product Name 5",
    price: "$149",
    discounted_price: "$199",
    add_to_cart_icon: "bi bi-bag-plus",
  },
  {
    image:
      "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
    brand: "Brand 6",
    name: "Product Name 6",
    price: "$149",
    discounted_price: "$199",
    add_to_cart_icon: "bi bi-bag-plus",
  },
];

const profile = {
  name: "John Doe",
  description: "I am a web developer",
  image:
    "https://images.unsplash.com/photo-1646753522408-077ef9839300?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8NjZ8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
  socials: [
    {
      name: "Twitter",
      icon: "bi bi-twitter",
      link: "https://twitter.com",
    },
    {
      name: "Facebook",
      icon: "bi bi-facebook",
      link: "https://facebook.com",
    },
    {
      name: "Instagram",
      icon: "bi bi-instagram",
      link: "https://instagram.com",
    },
  ],
};
</script>

<template>
  <div>
    <section class="w-full bg-gray-100 py-20">
      <div class="w-fit mx-auto flex flex-col items-center">
        <img
          :src="profile.image"
          alt="Profile"
          class="h-40 w-40 object-cover rounded-full"
        />
        <h1 class="text-3xl font-bold mt-5">{{ profile.name }}</h1>
        <p class="text-gray-500 mt-2">{{ profile.description }}</p>
        <div class="flex mt-5">
          <template v-for="social in profile.socials" :key="social.name">
            <a :href="social.link" class="mr-3">
              <svg
                :class="social.icon"
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                fill="currentColor"
                viewBox="0 0 16 16"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 1a7 7 0 0 0-7 7c0 3.86 3.14 7 7 7s7-3.14 7-7a7 7 0 0 0-7-7zm3.5 4.5a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5h-1v2a.5.5 0 0 1-1 0v-2h-1a.5.5 0 0 1-.5-.5v-3a.5.5 0 0 1 .5-.5h2zm-3 0a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h2z"
                />
              </svg>
            </a>
          </template>
        </div>
      </div>
    </section>
    <section
      id="Projects"
      class="w-fit mx-auto grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 justify-items-center justify-center gap-y-20 gap-x-14 mt-10 mb-5"
    >
      <template v-for="product in productList" :key="product.brand">
        <ProductCard v-bind="product" />
      </template>
    </section>
  </div>
</template>
