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
</script>

<template>
  <div>Profile Page</div>
  <section
    id="Projects"
    class="w-fit mx-auto grid grid-cols-1 lg:grid-cols-3 md:grid-cols-2 justify-items-center justify-center gap-y-20 gap-x-14 mt-10 mb-5"
  >
    <template v-for="product in productList" :key="product.brand">
      <ProductCard v-bind="product" />
    </template>
  </section>
</template>
