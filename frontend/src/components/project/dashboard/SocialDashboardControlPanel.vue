<template>
  <div class="control-panel">
    <div class="filter-buttons">
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
  },
  props: {
    downloadingInstantReport: {type: Boolean, default: false},
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
    downloadReportButtonIcon() {
      return this.downloadingInstantReport
        ? 'BaseButtonSpinner'
        : 'ReportsUploadIcon'
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
</style>
