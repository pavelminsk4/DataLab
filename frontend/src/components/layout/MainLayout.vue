<template>
  <div class="main-layout-wrapper">
    <MainHeader />
    <BackgroundIcon class="bg-icon" />
  </div>
</template>

<script>
import MainHeader from "@/components/navigation/MainHeader";

import BackgroundIcon from '../icons/BackgroundIcon'

export default {
  name: "MainLayout",
  components: {
    BackgroundIcon, MainHeader
  }
}
</script>

<style lang="scss" scoped>
  .main-layout-wrapper {
    position: relative;

    display: flex;
    justify-content: center;

    width: 100%;
    height: 100%;

    background-color: var(--primary-bg-color);

    .bg-icon {
      position: absolute;

      width: 66vw;
    }
  }
</style>