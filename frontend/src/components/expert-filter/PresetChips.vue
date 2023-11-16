<template>
  <BaseChips class="preset-chips" @click="toggleDropdown">
    <span>{{ presetName }}</span>

    <ArrowheadIcon :direction="isOpenPresetOptions ? 'top' : 'down'" />

    <DropdownOptionsContainer
      v-if="isOpenPresetOptions"
      :key="presetId"
      :options="dropDownOptions"
      @close-dropdown="toggleDropdown"
      @delete-preset="deletePreset"
    />
  </BaseChips>
</template>

<script>
import BaseChips from '@/components/BaseChips'
import ArrowheadIcon from '@components/icons/ArrowheadIcon'
import DropdownOptionsContainer from '@components/DropdownOptionsContainer'

export default {
  name: 'PresetChips',
  components: {BaseChips, ArrowheadIcon, DropdownOptionsContainer},
  props: {
    presetId: {type: Number, required: true},
    presetName: {type: String, required: true},
  },
  data() {
    return {
      isOpenPresetOptions: false,
    }
  },
  created() {
    this.dropDownOptions = [
      {name: 'Edit', icon: 'Edit', action: 'edit-preset'},
      {name: 'Delete', icon: 'Delete', action: 'delete-preset'},
    ]
  },
  methods: {
    toggleDropdown() {
      this.isOpenPresetOptions = !this.isOpenPresetOptions
    },
    deletePreset() {
      this.$emit('cancel-preset', this.presetId)
    },
  },
}
</script>

<style lang="scss" scoped>
.preset-chips {
  position: relative;
  overflow: visible;
  gap: 8px;

  background-color: #c3cdff;

  cursor: pointer;
}
</style>
