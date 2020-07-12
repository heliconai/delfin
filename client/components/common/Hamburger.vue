<template>
  <div
    v-on:click="$emit('click')"
    class="menu-button cursor-pointer z-10 position-relative flex justift-content-center align-items-center"
    v-bind:class="{open : open}"
  >
    <div class="menu-button__burger z-0"></div>
  </div>
</template>

<script>
export default {
    props: ['open']
}
</script>

<style>
.menu-button__burger {
  width: 30px;
  height: 3px;
  border-radius: 3px;
  transition: all 0.1s ease-in-out;
  background: #ffffff;
}
.menu-button__burger::before,
.menu-button__burger::after {
  content: '';
  position: absolute;
  width: 30px;
  height: 3px;
  border-radius: 3px;
  transition: all 0.1s ease-in-out;
  background: #ffffff;
}
.menu-button__burger::before {
  transform: translateY(-6px);
}
.menu-button__burger::after {
  transform: translateY(6px);
}
.menu-button.open .menu-button__burger {
    background: transparent;
}
.menu-button.open .menu-button__burger::before {
    transform: rotate(45deg);
}
.menu-button.open .menu-button__burger::after {
    transform: rotate(-45deg);
}
</style>