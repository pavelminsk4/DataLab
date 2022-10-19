<template>
  <section class="widget-layout-wrapper">
    <div class="widget-layout-wrapper__header">
      <div class="title">{{ title }}</div>

      <div class="setting-buttons">
        <div class="button" @click="openSettings"><SettingsIcon /></div>
        <div class="button" @click="deleteWidget"><CloseIcon /></div>
      </div>
    </div>
    <slot></slot>
  </section>
</template>

<script>
import SettingsIcon from '@/components/icons/SettingsIcon'
import CloseIcon from '@/components/icons/CloseIcon'

export default {
  name: 'WidgetsLayout',
  components: {CloseIcon, SettingsIcon},
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
    deleteWidget() {
      this.$emit('delete-widget')
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
    align-items: center;
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

    .setting-buttons {
      display: flex;
      gap: 8px;

      .button {
        cursor: pointer;

        display: flex;
        align-items: center;
        justify-content: center;

        width: 40px;
        height: 40px;

        background: var(--secondary-bg-color);
        border: 1px solid var(--input-border-color);
        border-radius: 10px;

        &:hover {
          background-color: var(--primary-button-color);
        }
      }
    }
  }
}
</style>
