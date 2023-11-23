<template>
  <section class="widget-layout-wrapper">
    <div class="widget-layout-wrapper__header">
      <CustomText :text="title" class="title" />

      <div class="setting-buttons">
        <div v-if="isShowSettingsBtn" class="button" @click="openSettingsModal">
          <SettingsIcon />
        </div>
        <div v-if="isShowDeleteBtn" class="button" @click="deleteWidget">
          <CrossIcon />
        </div>
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

import CustomText from '@components/CustomText'
import BaseSpinner from '@components/BaseSpinner'
import SettingsIcon from '@components/icons/SettingsIcon'
import CrossIcon from '@components/icons/CrossIcon'

export default {
  name: 'WidgetsLayout',
  components: {CrossIcon, BaseSpinner, SettingsIcon, CustomText},
  props: {
    title: {type: String, default: ''},
    widgetId: {type: Number, default: 0},
    isShowSettingsBtn: {type: Boolean, default: true},
    isShowDeleteBtn: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({loading: get.LOADING_WIDGETS}),
    isLoading() {
      return this.loading[this.widgetId] || false
    },
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
  --widget-layout-content-padding: 16px 20px 20px;

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

    border-bottom: var(--border-primary);

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
        border: var(--border-primary);
        border-radius: 4px;

        &:hover {
          color: var(--button-text-color);
          background-color: var(--button-primary-hover-color);
        }
      }
    }
  }

  &__content {
    width: 100%;
    height: 100%;
    padding: var(--widget-layout-content-padding);

    overflow: auto;
  }
}

.spinner {
  height: 100%;
  margin: auto;
}
</style>
