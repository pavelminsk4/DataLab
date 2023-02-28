<template>
  <div class="wrapper-button">
    <div
      v-for="button in mainSettings"
      :key="button"
      :class="[
        'general-button',
        panelSettingsName === button && 'general-button-active',
      ]"
      @click="toggleSettingsPanel"
    >
      {{ button }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsButtons',
  props: {
    isOnlyGeneral: {
      type: Boolean,
      default: false,
    },
    mainSettings: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      panelSettingsName: 'General',
    }
  },
  methods: {
    toggleSettingsPanel(e) {
      this.panelSettingsName = e.target.innerText
      this.$emit('update-setting-panel', this.panelSettingsName)
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

    padding: 4px 38px;
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
