<template>
  <div class="main-layout-wrapper">
    <div class="content">
      <MainHeader />

      <slot></slot>
    </div>
  </div>
</template>

<script>
import MainHeader from '@components/navigation/MainHeader'

export default {
  name: 'MainLayout',
  components: {
    MainHeader,
  },
}
</script>

<style lang="scss" scoped>
.main-layout-wrapper {
  position: relative;

  padding: 0 69px 60px 79px;
}

.content {
  z-index: 2;
}

.bg-icon {
  position: absolute;
  top: 40%;
  left: 50%;

  width: 66vw;

  z-index: 1;
  transform: translate(-50%, -50%);
}
</style>
