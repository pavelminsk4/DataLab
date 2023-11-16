<template>
  <div class="preset-bar">
    <CreateNewGroupModal
      v-if="isOpenCreateGroupModal"
      @close="closeGroupModal"
    />

    <PresetChips
      v-for="{id, title} in presets"
      :key="id"
      :preset-name="title"
      :preset-id="id"
    />

    <div class="points-button" @click="toggleDropdown">
      <PointsIcon />

      <DropdownOptionsContainer
        v-if="isOpenPresetsOptions"
        key="points-button"
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
import CreateNewGroupModal from '@/components/expert-filter/CreateNewGroupModal'

export default {
  name: 'PresetsBar',
  components: {
    DropdownOptionsContainer,
    PointsIcon,
    PresetChips,
    CreateNewGroupModal,
  },
  props: {
    presets: {type: Array, default: () => []},
  },
  data() {
    return {
      isOpenPresetsOptions: false,
      isOpenCreateGroupModal: false,
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
      this.isOpenCreateGroupModal = true
    },
    clearPresets() {
      console.log('CLEAR PRESETS')
    },
    closeGroupModal() {
      this.isOpenCreateGroupModal = false
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
