<template>
  <div class="wrapper-button">
    <div
      v-for="button in mainSettings"
      :key="button"
      :class="[
        'general-button',
        panelNameProxy === button && 'general-button-active',
      ]"
      @click="toggleSettingsPanel(button)"
    >
      <CustomText :text="button" />
    </div>
  </div>
</template>

<script>
import CustomText from '@components/CustomText'

export default {
  name: 'BaseTabs',
  components: {CustomText},
  props: {
    mainSettings: {type: Array, required: true},
    defaultTab: {type: String, required: true},
  },
  data() {
    return {
      panelName: '',
    }
  },
  computed: {
    panelNameProxy: {
      get() {
        return this.panelName || this.defaultTab
      },
      set(value) {
        this.panelName = value
      },
    },
  },
  methods: {
    toggleSettingsPanel(val) {
      this.panelName = val
      this.$emit('update-setting-panel', this.panelNameProxy)
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper-button {
  display: flex;
  justify-content: space-between;
  gap: 2px;

  padding: 4px;

  background: var(--background-secondary-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;

  cursor: pointer;

  .general-button {
    display: flex;
    align-items: center;
    justify-content: center;

    padding: 4px;
    width: 100%;

    text-align: center;

    &:hover {
      color: var(--button-text-color);
      background: var(--primary-hover-color);
      border-radius: 10px;
    }
  }

  .general-button-active {
    background: var(--primary-active-color);
    border-radius: 10px;
  }
}
</style>
