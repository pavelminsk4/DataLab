<template>
  <section class="widget-layout-wrapper">
    <div class="widget-layout-wrapper__header">
      <div class="title">{{ title }}</div>

      <div class="setting-buttons">
        <div v-if="isShowSettings" class="button" @click="openSettingsModal">
          <SettingsIcon />
        </div>
        <div class="button" @click="deleteWidget"><CrossIcon /></div>
      </div>
    </div>
    <div class="widget-layout-wrapper__content scroll">
      <BaseSpinner v-if="isLoading" class="spinner" />
      <slot v-else></slot>
    </div>
  </section>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import BaseSpinner from '@/components/BaseSpinner'
import SettingsIcon from '@/components/icons/SettingsIcon'
import CrossIcon from '@/components/icons/CrossIcon'

export default {
  name: 'WidgetsLayout',
  components: {CrossIcon, BaseSpinner, SettingsIcon},
  props: {
    title: {
      type: String,
      default: '',
    },
    isShowSettings: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING}),
  },
  methods: {
    openSettingsModal() {
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
  align-items: center;

  min-width: 100%;
  height: 100%;

  border-radius: 8px;
  background-color: var(--background-secondary-color);
  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);

  color: var(--typography-primary-color);

  &__header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    width: 100%;
    padding: 12px 20px;

    border-bottom: 1px solid var(--border-color);

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

        width: 28px;
        height: 28px;

        background: var(--background-secondary-color);
        border: 1px solid var(--border-color);
        border-radius: 4px;

        &:hover {
          color: var(--button-text-color);
          background-color: var(--button-primary-hover-color);
        }
      }
    }
  }

  &__content {
    padding: 16px 20px 20px;

    overflow: auto;
  }
}

.spinner {
  height: 100%;
}
</style>
