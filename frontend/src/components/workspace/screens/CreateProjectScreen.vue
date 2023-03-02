<template>
  <MainLayoutTitleBlock
    title="The Project"
    description="Name the project and choose source Type"
    :back-page="{
      name: 'main page',
      routName: 'OnlineHome',
    }"
  />

  <ProgressBar />

  <div class="form-wrapper">
    <h4 class="label">Name</h4>
    <BaseInput :placeholder="'Project Name'" v-model="projectName" />

    <h4 class="label">Description</h4>
    <BaseTextarea
      v-model="description"
      placeholder="Some words about your project"
    />

    <BaseButton
      :is-disabled="!projectName"
      class="next-button"
      @click="nextStep"
    >
      <span>Next</span>
      <ArrowLeftIcon class="button-arrow-icon" />
    </BaseButton>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProgressBar from '@/components/workspace/ProgressBar'

export default {
  name: 'CreateProjectScreen',
  components: {
    ArrowLeftIcon,
    BaseButton,
    BaseInput,
    BaseTextarea,
    MainLayoutTitleBlock,
    ProgressBar,
  },
  props: {
    workspaceId: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      projectName: '',
      description: '',
    }
  },
  computed: {
    ...mapState(['currentStep', 'userInfo']),
  },
  created() {
    if (
      this.workspaceId !== 'new' &&
      this.currentStep === 'OnlineWorkspaceStep2'
    )
      this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([
      action.UPDATE_PROJECT_STATE,
      action.UPDATE_CURRENT_STEP,
      action.CLEAR_STATE,
    ]),
    nextStep() {
      try {
        this[action.UPDATE_CURRENT_STEP]('OnlineWorkspaceStep3')
        this[action.UPDATE_PROJECT_STATE]({
          creator: this.userInfo.id,
          title: this.projectName,
          description: this.description,
          source: 'Online',
          workspace: this.workspaceId || null,
        })
        this.$router.push({
          name: 'OnlineWorkspaceStep3',
          params: {workspaceId: this.workspaceId},
        })
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 56%;
  margin-top: 40px;
}
.label {
  margin: 20px 0 4px;

  font-weight: 400;

  &:first-child {
    margin-top: 0;
  }
}

.next-button {
  align-self: flex-end;

  margin-top: 32px;

  .button-arrow-icon {
    margin-left: 10px;
    transform: rotate(180deg);
  }
}
</style>
