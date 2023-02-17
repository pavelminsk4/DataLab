<template>
  <!-- <NavigationBar
    v-if="currentStep === 'Step2'"
    :step="step"
    title="Create Project"
    hint="Name the project and choose source Type"
    :is-active-button="!!projectName && !!selectedValue.name"
    @next-step="nextStep"
  />

  <NavigationBar
    v-else
    :step="step"
    title="Create Project"
    hint="Name the project and choose source Type"
    :is-existing-workspace="true"
    :is-active-button="!!projectName && !!selectedValue.name"
    @next-step="nextStepForExistingWorkspace"
  /> -->

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
  data() {
    return {
      projectName: '',
      description: '',
    }
  },
  created() {
    if (this.step === 'ProjectStep1') this[action.CLEAR_STATE]()
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
      try {
        this[action.UPDATE_CURRENT_STEP]('Step3')
        this[action.UPDATE_PROJECT_STATE]({
          creator: this.userInfo.id,
          title: this.projectName,
          description: this.description,
          source: 'Online',
        })
        this.$router.push({
          name: 'Step3',
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
