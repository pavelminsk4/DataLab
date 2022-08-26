<template>
  <div class="main-layout-wrapper">
    <BackgroundIcon class="bg-icon" />

    <div class="content">
      <MainHeader />

      <slot></slot>
    </div>
  </div>
</template>

<script>
import MainHeader from '@components/navigation/MainHeader'
import BackgroundIcon from '@components/icons/BackgroundIcon'

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

    height: 100vh;
    padding: 0 69px 0 79px;

    background-color: var(--primary-bg-color);
  }

  .bg-icon {
    position: absolute;
    top:40%;
    left:50%;

    width: 66vw;

    transform:translate(-50%, -50%);
  }
</style>
