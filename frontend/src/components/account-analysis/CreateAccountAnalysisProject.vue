<template>
  <div class="form-wrapper">
    <AccountAnalysisSourcesTabs />

    <BaseInput
      v-model="projectName"
      label="Name"
      placeholder="Project Name"
      class="input-name"
    />

    <div>Profile</div>

    <BaseSelect
      v-model="profileHandle"
      :options="profileOptions"
      select-name="profile-handle"
    >
      <li
        v-for="(option, index) in profileOptions"
        :key="option.user_alias + index"
        @click="handleClick"
      >
        <img :src="option.user_picture" alt="User picture" />
        {{ option.user_alias }}
      </li>
    </BaseSelect>

    <footer>
      <ButtonWithArrow :is-disabled="!projectName" @click="saveChanges">
        <span>Save Project</span>
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapState, mapActions, createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'

import BaseInput from '@/components/common/BaseInput'
import BaseSelect from '../BaseSelect2.vue'
import AccountAnalysisSourcesTabs from '@/components/account-analysis/AccountAnalysisSourcesTabs'

const {
  mapActions: mapAccountAnalysisActions,
  mapState: mapAccountAnalysisState,
} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'CreateAccountAnalysisProject',
  mixins: [createReportMixin],
  components: {
    BaseInput,
    BaseSelect,
    AccountAnalysisSourcesTabs,
  },
  data() {
    return {
      projectName: '',
      profileHandle: '',
      selectedUsers: [],
      errors: {
        usersEmailError: null,
        projectName: null,
      },
    }
  },
  computed: {
    ...mapState({
      newWorkspace: (state) => state.newAccountAnalysisWorkspace,
      newProject: (state) => state.newAccountAnalysisProject,
    }),
    ...mapAccountAnalysisState({
      profileHandleOptions: (state) => state.listOfProfileHandle,
    }),
    profileOptions() {
      return this.profileHandleOptions
    },
  },
  created() {
    this[action.GET_LIST_OF_PROFILE_HANDLE]()
  },
  methods: {
    ...mapActions([action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT]),
    ...mapAccountAnalysisActions([
      action.GET_LIST_OF_PROFILE_HANDLE,
      action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE,
      action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT,
    ]),
    handleClick({target}) {
      this.profileHandle = target.innerText
    },
    async saveChanges() {
      await this[action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({
        title: this.projectName,
        profile_handle: this.profileHandle,
        source_filter: 'twitter',
      })
      await this[action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE]({
        ...this.newWorkspace,
        projects: [
          {
            ...this.newProject,
            title: this.projectName,
            profile_handle: this.profileHandle,
            source_filter: ['twitter'],
            members: [1],
          },
        ],
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 90%;
  margin-top: 40px;
}

.input-name {
  margin-bottom: 32px;
}

.report-add-users {
  width: 100%;
  margin-top: 32px;
}
</style>
