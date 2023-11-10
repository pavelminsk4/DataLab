<template>
  <div class="action-buttons">
    <BaseTooltipSettings>
      <button
        :class="['action-button', isInactive && 'disable']"
        @click.stop="$emit('stop-collecting-data')"
      >
        <StopIcon class="action-icon" />
        <div>Stop collecting data</div>
      </button>
      <button class="action-button" @click.stop="$emit('delete-entity')">
        <DeleteIcon class="action-icon" /> Delete
      </button>
    </BaseTooltipSettings>
  </div>
</template>

<script>
import StopIcon from '@/components/icons/StopIcon'
import DeleteIcon from '@/components/icons/DeleteIcon'
import BaseTooltipSettings from '@/components/BaseTooltipSettings'

export default {
  name: 'ProjectsTableActions',
  components: {StopIcon, DeleteIcon, BaseTooltipSettings},
  props: {status: {type: String, required: false}},
  computed: {
    isInactive() {
      return this.status === 'inactive'
    },
  },
}
</script>

<style lang="scss" scoped>
.action-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  width: 80px;

  .action-button {
    display: flex;
    align-items: center;

    gap: 10px;
    padding: 6px 10px;
    flex-shrink: 0;

    background: none;
    border: none;

    cursor: pointer;

    color: var(--typography-primary-color);

    &:hover {
      background: var(--primary-hover-color);
      border-radius: 12px;

      color: var(--button-text-color);

      .action-icon {
        color: var(--button-text-color);
      }
    }

    .action-icon {
      width: 24px;
      height: 24px;
    }
  }
}
</style>
