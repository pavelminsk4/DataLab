<template>
  <div class="chips-statuses-wrapper">
    <div
      v-for="(status, index) in statuses"
      :key="'chips-status-' + index"
      :class="['status-chips', currentStatus === status && 'active-chips']"
      @click="showStatusCards(status)"
    >
      {{ status }}
    </div>
  </div>
</template>

<script>
import {defaultStatuses} from '@/lib/configs/tfsStatusesConfig'

export default {
  name: 'StatusesChips',
  data() {
    return {
      currentStatus: null,
    }
  },
  computed: {
    statuses() {
      return defaultStatuses
    },
  },
  methods: {
    showStatusCards(status) {
      if (this.currentStatus === status) {
        this.currentStatus = null
        return this.$emit('show-status-cards', null)
      }

      this.currentStatus = status
      this.$emit('show-status-cards', status)
    },
  },
}
</script>

<style lang="scss" scoped>
.chips-statuses-wrapper {
  display: flex;
  gap: 12px;
  .status-chips {
    padding: 6px 8px;

    border-radius: 2px 12px 12px 2px;
    background-color: var(--background-additional-color);

    cursor: pointer;

    font-size: 12px;
  }

  .active-chips {
    color: var(--button-text-color);
    background-color: var(--button-primary-color);
  }
}
</style>
