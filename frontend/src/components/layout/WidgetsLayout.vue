<template>
  <section class="widget-layout-wrapper">
    <div class="widget-layout-wrapper__header">
      <div class="title">{{ title }}</div>
    </div>
    <slot></slot>
  </section>
</template>

<script>
export default {
  name: 'WidgetsLayout',
  props: {
    title: {
      type: String,
      default: '',
    },
  },
}
</script>

<style lang="scss" scoped>
.widget-layout-wrapper {
  display: flex;
  flex-direction: column;

  min-width: 100%;
  min-height: 100%;
  padding: 12px 20px 35px;

  &__header {
    width: 100%;
    padding-bottom: 12px;

    border-bottom: 1px solid var(--input-border-color);

    .title {
      font-style: normal;
      font-weight: 600;
      font-size: 16px;
      line-height: 22px;
    }
  }
}
</style>
