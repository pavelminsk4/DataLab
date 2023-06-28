<template>
  <div class="form-wrapper">
    <BaseInput
      v-model="projectName"
      label="Name"
      placeholder="Project Name"
      class="input-name-field"
    />

    <BaseTextarea
      v-model="projectDescription"
      placeholder="Some words about project"
      label="Description"
      class="input-name-field"
    />

    <footer class="create-project__footer">
      <ButtonWithArrow
        :is-disabled="!projectName"
        class="button"
        @click="nextStep"
      >
        <span>Next</span>
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'
import ComparisonMixin from '@/lib/mixins/comparison.js'

export default {
  name: 'CreateComparisonProject',
  mixins: [ComparisonMixin],
  props: {
    workspaceId: {type: String, default: null},
    moduleName: {type: String, default: ''},
  },
  data() {
    return {
      projectName: '',
      projectDescription: '',
    }
  },
  computed: {
    ...mapState(['userInfo']),
  },
  created() {
    if (
      this.workspaceId !== 'new' &&
      this.currentStep === 'ComparisonWorkspaceStep2'
    )
      this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.CLEAR_STATE]),

    nextStep() {
      const nextStep = 3
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_COMPARISON_WORKSPACE]({step: 3})

      this[action.UPDATE_NEW_COMPARISON_PROJECT]({
        creator: this.userInfo.id,
        members: [this.userInfo.id],
        title: this.projectName,
        description: this.projectDescription,
        source: this.moduleName,
        workspace: +this.workspaceId ? this.workspaceId : null,
      })
      this.$router.push({name: nextStepName})
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 75%;
  margin-top: 40px;
  gap: 15px;

  .input-name-field {
    margin-bottom: 32px;
  }

  .create-project__footer {
    display: flex;
    justify-content: flex-end;
  }
}
</style>
