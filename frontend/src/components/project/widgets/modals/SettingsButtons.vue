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
  data() {
    return {
      panelSettingsName: 'General',
      mainSettings: ['General', 'Dimensions'],
    }
  },
  methods: {
    toggleSettingsPanel(e) {
      this.panelSettingsName =
        this.panelSettingsName === e.target.innerText
          ? null
          : e.target.innerText

      this.$emit('update-setting-panel', this.panelSettingsName)
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper-button {
  display: flex;

  padding-bottom: -10px;

  border-bottom: 1px solid var(--input-border-color);

  cursor: pointer;

  .general-button {
    margin-right: 40px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;

    color: rgba(255, 255, 255, 0.8);
  }

  .general-button-active {
    padding-bottom: 10px;

    border-bottom: 1px solid var(--primary-button-color);

    color: var(--primary-text-color);
  }
}
</style>
