<template>
  <div class="control-panel">
    <div class="filter-buttons">
      <BaseDropdown name="sort-posts" class="sorting-dropdown">
        <template #selectedValue>
          <div class="sorting-dropdown-title">
            <SortIcon class="sort-icon" />{{ capitalizeFirstLetter(sortValue) }}
          </div>
        </template>
        <CustomText
          v-for="(item, index) in sortingList"
          :key="item + index"
          :text="snakeCaseToSentenseCase(item)"
          class="sorting-item"
          @click="$emit('set-sorting-value', item)"
        />
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
import {capitalizeFirstLetter, snakeCaseToSentenseCase} from '@/lib/utilities'

import CustomText from '@/components/CustomText'
import PlusIcon from '@/components/icons/PlusIcon'
import SortIcon from '@/components/icons/SortIcon'
import FiltersIcon from '@/components/icons/FiltersIcon'
import ExpertFilterIcon from '@/components/icons/ExpertFilterIcon'
import BaseDropdown from '@/components/BaseDropdown'
import BaseButton from '@/components/common/BaseButton'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'

export default {
  name: 'OnlineDashboardControlPanel',
  components: {
    BaseDropdown,
    CustomText,
    PlusIcon,
    SortIcon,
    BaseButton,
    BaseButtonSpinner,
    ReportsUploadIcon,
    FiltersIcon,
    ExpertFilterIcon,
  },
  props: {
    sortValue: {type: String, required: true},
    downloadingInstantReport: {type: Boolean, default: false},
  },
  computed: {
    filtersList() {
      return [
        {
          name: 'Filter',
          modalName: 'isOpenFilterModal',
          background: '#F2E5FF',
          color: '#4B0096',
          icon: 'FiltersIcon',
        },
        {
          name: 'Expert Filter',
          modalName: 'isOpenExpertFilterModal',
          background: '#E0F5FF',
          color: '#006496',
          icon: 'ExpertFilterIcon',
        },
      ]
    },
    sortingList() {
      return [
        'country',
        'language',
        'source',
        'potential_reach_desc',
        'potential_reach',
        'date_desc',
        'date',
      ]
    },
    downloadReportButtonIcon() {
      return this.downloadingInstantReport
        ? 'BaseButtonSpinner'
        : 'ReportsUploadIcon'
    },
  },
  methods: {
    capitalizeFirstLetter,
    snakeCaseToSentenseCase,
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

    .sort-icon {
      color: var(--sorting-primary-color);
    }
  }

  .sorting-item {
    &:hover {
      color: var(--sorting-primary-color);
      background-color: var(--sorting-background-primary-color);
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
