<template>
  <div class="control-panel">
    <div class="filter-buttons">
      <BaseDropdown name="sort-posts" class="sorting-dropdown">
        <template #selectedValue>
          <div class="sorting-dropdown-title">
            <component
              :is="`${sortIcon.name}Icon`"
              :direction="sortIcon.direction"
              class="icon"
            />
            {{ sortingValue }}
          </div>
        </template>
        <div
          v-for="(item, index) in sortingList"
          :key="item.value + index"
          class="sorting-item"
          @click="setSortingValue(item)"
        >
          <CustomText :text="item.name" class="sorting-name" />
          <component
            :is="`${item.icon}Icon`"
            :direction="item.direction"
            class="icon"
          />
        </div>
      </BaseDropdown>

      <div
        v-for="(item, index) in filtersList"
        :key="item + index"
        :style="`background-color: ${item.background}; color: ${item.color}`"
        class="filter-button"
        @click="$emit('open-modal', item.modalName)"
      >
        <component :style="`color: ${item.color}`" :is="item.icon" />{{
          item.name
        }}
      </div>
    </div>

    <div class="menu-buttons">
      <BaseButton
        :is-not-background="true"
        class="button-upload"
        @click="$emit('download-report')"
      >
        <component :is="downloadReportButtonIcon" style="--spinner-width: 16px">
        </component>
        <CustomText text="Download Report" />
      </BaseButton>

      <BaseButton class="button" @click="$emit('open-widgets-list-modal')">
        <PlusIcon class="icon" />
        <CustomText text="Add Widgets" />
      </BaseButton>
    </div>
  </div>
</template>

<script>
import CustomText from '@components/CustomText'
import ArrowLongIcon from '@components/icons/ArrowLongIcon'
import PlusIcon from '@components/icons/PlusIcon'
import SortIcon from '@components/icons/SortIcon'
import FiltersIcon from '@components/icons/FiltersIcon'
import ExpertFilterIcon from '@components/icons/ExpertFilterIcon'
import BaseButton from '@components/common/BaseButton'
import BaseButtonSpinner from '@components/BaseButtonSpinner'
import ReportsUploadIcon from '@components/icons/ReportsUploadIcon'
import BaseDropdown from '@components/BaseDropdown'

export default {
  name: 'SocialDashboardControlPanel',
  components: {
    CustomText,
    PlusIcon,
    SortIcon,
    BaseButton,
    ArrowLongIcon,
    BaseButtonSpinner,
    ReportsUploadIcon,
    FiltersIcon,
    ExpertFilterIcon,
    BaseDropdown,
  },
  props: {
    downloadingInstantReport: {type: Boolean, default: false},
  },
  data() {
    return {
      sortIcon: {name: 'Sort', derection: ''},
      sortingValue: 'Latest',
    }
  },
  computed: {
    filtersList() {
      return [
        {
          name: 'Filter',
          modalName: 'SocialFiltersModal',
          background: '#F2E5FF',
          color: '#4B0096',
          icon: 'FiltersIcon',
        },
        {
          name: 'Expert Filter',
          modalName: 'ExpertFilterModal',
          background: '#E0F5FF',
          color: '#006496',
          icon: 'ExpertFilterIcon',
        },
      ]
    },
    sortingList() {
      return [
        {
          value: 'potential_reach_desc',
          name: 'Potential Reach',
          icon: 'ArrowLong',
        },
        {
          value: 'potential_reach',
          name: 'Potential Reach',
          icon: 'ArrowLong',
          direction: 'top',
        },
      ]
    },
    downloadReportButtonIcon() {
      return this.downloadingInstantReport
        ? 'BaseButtonSpinner'
        : 'ReportsUploadIcon'
    },
  },
  methods: {
    setSortingValue(sortValue) {
      this.sortIcon = {name: sortValue.icon, direction: sortValue.direction}
      this.sortingValue = sortValue.name
      this.$emit('set-sorting-value', sortValue.value)
    },
  },
}
</script>

<style lang="scss" scoped>
.control-panel {
  display: flex;
  justify-content: space-between;

  width: 100%;

  .filter-buttons {
    display: flex;
    align-items: center;

    gap: 16px;

    .filter-button {
      display: flex;

      gap: 4px;
      padding: 4px 12px;

      border-radius: 12px;

      cursor: pointer;
    }
  }

  .menu-buttons {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 40px;

    .button-upload {
      gap: 15px;
      padding: 0 20px;

      font-size: 14px;
      line-height: 20px;
    }

    .button {
      width: 155px;

      .icon {
        margin-right: 10px;
      }
    }
  }
}
.sorting-dropdown {
  padding: 4px 8px;

  border-radius: 12px;
  background-color: var(--sorting-background-primary-color);

  .sorting-dropdown-title {
    display: flex;
    align-items: center;

    gap: 4px;
    margin-right: 4px;

    color: var(--sorting-primary-color);
  }

  .icon {
    color: var(--sorting-primary-color);
  }

  .sorting-item {
    display: flex;
    align-items: center;

    &:hover {
      color: var(--sorting-primary-color);
      background-color: var(--sorting-background-primary-color);

      .sorting-name {
        color: var(--sorting-primary-color);
        background-color: var(--sorting-background-primary-color);
      }
    }
  }
}
</style>

<style lang="scss">
.sorting-dropdown .container-placeholder {
  .title,
  .arrow-down {
    color: var(--sorting-primary-color);
  }
}
</style>
