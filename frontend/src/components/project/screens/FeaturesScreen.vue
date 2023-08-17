<template>
  <div class="features">
    <div class="features__header">
      <MainLayoutTitleBlock
        :title="currentProject.title"
        :description="currentProject.note"
        :back-page="{
          name: 'workspace',
          routeName: `${currentProject.source}Workspace`,
        }"
        :should-translate="false"
      >
        <TotalResults :total-results="numberOfPosts" />
      </MainLayoutTitleBlock>
      <BaseButton :is-not-background="true" class="btn-report">
        <ReportsUploadIcon />
        <CustomText text="Download Report" />
      </BaseButton>
    </div>
    <router-view :current-project="currentProject"></router-view>
  </div>
</template>

<script>
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import BaseButton from '@/components/common/BaseButton'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import TotalResults from '@/components/TotalResults'
import CustomText from '@/components/CustomText'

export default {
  name: 'FeaturesScreen',
  components: {
    MainLayoutTitleBlock,
    BaseButton,
    ReportsUploadIcon,
    TotalResults,
    CustomText,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    numberOfPosts: {type: Number, required: true},
  },
}
</script>

<style lang="scss" scoped>
.features {
  display: flex;
  flex-direction: column;
  gap: 30px;

  padding-bottom: 20px;
}
.features__header {
  display: flex;
  justify-content: space-between;

  .btn-report {
    align-self: flex-end;
  }
}
</style>
