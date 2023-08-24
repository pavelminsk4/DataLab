<template>
  <div class="preset-bar">
    <PresetChips
      v-for="{id, name} in presets"
      :key="id"
      :preset-name="name"
      :preset-id="id"
    />

    <div class="points-button" @click="toggleDropdown">
      <PointsIcon />

      <DropdownOptionsContainer
        v-if="isOpenPresetsOptions"
        :options="presetsOptions"
        @close-dropdown="toggleDropdown"
        @save-group="saveGroup"
        @clear-presets="clearPresets"
      />
    </div>
  </div>
</template>

<script>
import PointsIcon from '@/components/icons/PointsIcon'
import PresetChips from '@components/expert-filter/PresetChips'
import DropdownOptionsContainer from '@components/DropdownOptionsContainer'

export default {
  name: 'PresetsBar',
  components: {DropdownOptionsContainer, PointsIcon, PresetChips},
  props: {
    presets: {type: Array, default: () => []},
  },
  data() {
    return {
      isOpenPresetsOptions: false,
    }
  },
  created() {
    this.presetsOptions = [
      {name: 'Save groupe', icon: 'Save', action: 'save-group'},
      {name: 'Clear All', icon: 'Delete', action: 'clear-presets'},
    ]
  },
  methods: {
    toggleDropdown() {
      this.isOpenPresetsOptions = !this.isOpenPresetsOptions
    },
    saveGroup() {
      console.log('SAVE GROUP')
    },
    clearPresets() {
      console.log('CLEAR PRESETS')
    },
  },
}
</script>

<style lang="scss" scoped>
.preset-bar {
  display: flex;
  align-items: center;
  gap: 8px;
}

.points-button {
  position: relative;

  display: flex;
  justify-content: center;
  align-items: center;

  width: 28px;
  height: 28px;

  background-color: var(--background-secondary-color);
  border-radius: 4px;
  border: var(--border-primary);

  cursor: pointer;
}
</style>
