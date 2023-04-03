<template>
  <div class="main-layout">
    <MainHeader />
    <section class="two-columns-wrapper">
      <div class="content scroll">
        <slot></slot>
      </div>

      <div
        v-if="isTwoColumns"
        :style="`--width-second-column: ${widthSecondColumns}`"
        class="second-column"
      >
        <slot name="second-column"></slot>
      </div>
    </section>
  </div>
</template>

<script>
import MainHeader from '@components/navigation/MainHeader'

export default {
  name: 'MainLayout',
  components: {
    MainHeader,
  },
  props: {
    isTwoColumns: {type: Boolean, default: false},
    widthSecondColumns: {type: String, default: '100%'},
  },
}
</script>

<style lang="scss">
.main-layout {
  position: relative;

  display: flex;

  padding-top: var(--header-height);
  width: 100vw;
  height: 100vh;

  &__section {
    width: 100%;
  }
}
</style>

<style lang="scss" scoped>
.two-columns-wrapper {
  display: flex;

  width: 100%;
  height: 100%;
}

.second-column {
  width: var(--width-second-column);

  background-color: var(--background-secondary-color);
}

.content {
  z-index: 2;

  overflow: auto;

  width: 100%;
  height: 100%;
  padding: 24px 32px;
}
</style>
