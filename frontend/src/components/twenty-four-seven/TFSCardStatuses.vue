<template>
  <div
    class="dropdown-statuses-wrapper"
    :id="`dropdown-statuses-${postId}`"
    @click="openDropdown"
  >
    <div class="statuses-wrapper">
      <div :style="`background-color: ${statuses[status].color}`" class="title">
        {{ getTitle(status) }}
      </div>
      <div
        v-if="statuses[status].availableStatusesForMoving.length"
        :style="`background-color: ${statuses[status].color}`"
        class="icon-wrapper"
      >
        <ArrowDownIcon class="arrow-icon" />
      </div>
    </div>

    <ul
      v-if="isOpen && statuses[status].availableStatusesForMoving.length"
      class="dropdown"
    >
      <li
        v-for="option in statuses[status].availableStatusesForMoving"
        :key="option"
        class="item"
        @click="changeStatus(option.title)"
      >
        <div
          :style="`background-color: ${option.color}`"
          class="status-color"
        />
        {{ option.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import {cardStatuses} from '@/lib/configs/tfsStatusesConfig'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  name: 'TFSCardStatuses',
  components: {
    ArrowDownIcon,
  },
  props: {
    isBack: {type: Boolean, default: true},
    postId: {type: Number, reqired: true},
    status: {type: String, reqired: true},
  },
  data() {
    return {
      dropdownStatusesItems: [],
      isOpen: false,
    }
  },
  created() {
    this.statuses = cardStatuses
    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    openDropdown() {
      this.isOpen = !this.isOpen
    },
    closeDropdown({target}) {
      const dropdownList = document.getElementById(
        `dropdown-statuses-${this.postId}`
      )

      if (!dropdownList?.contains(target)) {
        this.isOpen = false
      }
    },
    changeStatus(newStatus) {
      this.$emit('change-status-card', newStatus)
    },
    getTitle(status) {
      return this.isBack ? 'Back to ' + status.toLowerCase() : status
    },
  },
}
</script>

<style lang="scss" scoped>
.dropdown-statuses-wrapper {
  position: relative;

  cursor: pointer;
  .statuses-wrapper {
    display: flex;
    gap: 2px;

    cursor: pointer;

    .title {
      padding: 6px 8px;

      border-radius: 4px;

      font-style: normal;
      font-weight: 400;
      font-size: 11px;
      line-height: 12px;
      color: var(--background-secondary-color);
    }

    .icon-wrapper {
      display: flex;
      align-items: center;
      justify-content: center;

      padding: 6px 8px;

      border-radius: 4px;

      .arrow-icon {
        width: 8px;
        height: 8px;

        transform: rotate(-90deg);
        color: var(--background-secondary-color);
      }
    }
  }

  .dropdown {
    display: flex;
    flex-direction: column;

    position: absolute;

    margin-top: 5px;
    padding: 10px;

    background: var(--background-secondary-color);
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);
    border-radius: 8px;

    list-style: none;
    z-index: 2;

    .item {
      display: flex;
      align-items: center;
      gap: 10px;

      padding: 12px 10px;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-primary-color);

      &:hover {
        border-radius: 4px;
        background-color: var(--primary-active-color);
      }
      .status-color {
        width: 16px;
        height: 16px;

        border-radius: 4px;
      }
    }
  }
}
</style>
