<template>
  <div class="px-5 py-5 w-full bg-transparent absolute z-50">
    <div class="container flex items-center justify-between">
      <div class="flex items-center hover:opacity-50 cursor-pointer" href="/">
        <Logo class="h-9 w-9" />
        <div class="text-white font-fredoka text-2xl">delfin</div>
      </div>
      <Hamburger class="sm:hidden" @click="toggleNavbar" :open="showMenu" />
      <div class="flex hidden sm:flex items-center justify-between space-x-5">
        <a
          class="flex text-white text-right font-semibold text-lg hover:text-medium-turquoise rounded"
          href="/docs"
        >Docs</a>
        <a
          class="flex text-white text-right font-semibold text-lg hover:text-medium-turquoise rounded"
          href="#"
        >GitHub</a>
        <a
          class="flex text-white text-right font-semibold text-lg hover:text-medium-turquoise rounded"
          href="#"
        >Features</a>
      </div>
      <button
        class="flex items-center bg-medium-turquoise px-4 py-1 text-rich-black text-right font-semibold text-lg hover:bg-bittersweet hover:text-white rounded-full"
        href="/login"
      >
        Login
        <span class="material-icons ml-2">launch</span>
      </button>
    </div>
    <div
      class="block menu relative mt-2 w-full rounded-lg bg-white z-50 shadow-2xl focus:shadow-outline"
      v-bind:class="showMenu ? 'show-menu' : 'hide'"
    >
      <a
        class="block text-center font-semibold py-2 text-xl hover:bg-medium-turquoise rounded-lg"
        href="/docs"
      >Docs</a>
      <a
        class="block text-center font-semibold py-2 text-xl hover:bg-medium-turquoise rounded-lg"
        href="#"
      >GitHub</a>
    </div>
  </div>
</template>

<script>
import Logo from '@/components/common/Logo'
import Hamburger from '@/components/common/Hamburger'
export default {
  data() {
    return {
      showMenu: false
    }
  },
  methods: {
    toggleNavbar: function(){
      this.showMenu = !this.showMenu;
    }
  }
}
</script>
<style>
.menu {
  visibility: visible;
  opacity: 1;
  transition: all 0.2s ease-in-out;
}

.menu.hide {
  visibility: hidden;
  opacity: 0;
}
</style>