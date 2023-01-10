<template>
  <section class="widget-layout-wrapper scroll">
    <div class="widget-layout-wrapper__header">
      <div class="title">{{ title }}</div>

      <div class="setting-buttons">
        <div v-if="isShowSettings" class="button" @click="openSettings">
          <SettingsIcon />
        </div>
        <div class="button" @click="deleteWidget"><CloseIcon /></div>
      </div>
    </div>
    <BaseSpinner v-if="isLoading" />
    <slot v-else></slot>
  </section>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import BaseSpinner from '@/components/BaseSpinner'
import CloseIcon from '@/components/icons/CloseIcon'
import SettingsIcon from '@/components/icons/SettingsIcon'

export default {
  name: 'WidgetsLayout',
  components: {BaseSpinner, CloseIcon, SettingsIcon},
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
  align-items: center;

  min-width: 100%;
  height: fit-content;
  max-height: 100%;
  padding: 20px;

  border-radius: 8px;
  border: 1px solid var(--input-border-color);
  background-color: var(--secondary-bg-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

  color: var(--primary-text-color);

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
