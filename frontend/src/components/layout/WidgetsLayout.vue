<template>
  <section class="widget-layout-wrapper">
    <div class="widget-layout-wrapper__header">
      <div class="title">{{ title }}</div>
      <div class="settings" @click="openSettings"><SettingsIcon /></div>
    </div>
    <slot></slot>
  </section>
</template>

<script>
import SettingsIcon from '@/components/icons/SettingsIcon'
export default {
  name: 'WidgetsLayout',
  components: {SettingsIcon},
  props: {
    title: {
      type: String,
      default: '',
    },
  },
  methods: {
    openSettings() {
      this.$emit('open-modal')
    },
  },
}
</script>

<style lang="scss" scoped>
.widget-layout-wrapper {
  position: relative;

  display: flex;
  flex-direction: column;

  min-width: 100%;
  min-height: 100%;
  padding: 12px 20px 35px;

  &__header {
    display: flex;
    justify-content: space-between;

    width: 100%;
    padding-bottom: 12px;

    border-bottom: 1px solid var(--input-border-color);

    .title {
      font-style: normal;
      font-weight: 600;
      font-size: 16px;
      line-height: 22px;
    }

    .settings {
      cursor: pointer;

      display: flex;
      align-items: center;
      justify-content: center;

      width: 40px;
      height: 40px;

      background: var(--secondary-bg-color);
      border: 1px solid var(--input-border-color);
      border-radius: 10px;
    }
  }
}
</style>
