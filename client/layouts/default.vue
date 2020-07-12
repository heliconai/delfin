<template>
  <div class="flex flex-col h-screen justify-between">
    <Navbar />
    <Nuxt />
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/common/Navbar'
export default {
  components: {
    Navbar
  }
}
</script>