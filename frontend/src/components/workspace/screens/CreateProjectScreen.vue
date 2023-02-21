<template>
  <MainLayoutTitleBlock
    title="The Project"
    description="Name the project and choose source Type"
    :back-page="{
      name: 'main page',
      routName: 'Home',
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
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'
import BaseTextarea from '@/components/BaseTextarea'
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
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      projectName: '',
      description: '',
    }
  },
  created() {
    if (this.step === 'WorkspaceStep2') this[action.CLEAR_STATE]()
  },
  computed: {
    ...mapState(['currentStep', 'userInfo']),
  },
  methods: {
    ...mapActions([
      action.UPDATE_PROJECT_STATE,
      action.UPDATE_CURRENT_STEP,
      action.CLEAR_STATE,
    ]),
    nextStep() {
      const nextStep = this.workspaceId ? 'WorkspaceStep3' : 'Step3'
      try {
        this[action.UPDATE_CURRENT_STEP](nextStep)
        this[action.UPDATE_PROJECT_STATE]({
          creator: this.userInfo.id,
          title: this.projectName,
          description: this.description,
          source: 'Online',
          workspace: this.workspaceId?.toString() || null,
        })
        this.$router.push({
          name: nextStep,
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
