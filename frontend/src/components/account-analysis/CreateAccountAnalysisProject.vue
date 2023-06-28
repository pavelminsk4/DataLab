<template>
  <div class="form-wrapper">
    <AccountAnalysisSourcesTabs class="tabs" />

    <BaseInput
      v-model="projectName"
      label="Name"
      placeholder="Project Name"
      class="input-name-field"
    />

    <div class="title">Profile</div>
    <BaseSearchField
      v-model="accountProfile"
      name="profile-handle-search"
      placeholder="Enter profile handle"
      :list="profileNames"
      :is-search="true"
      :current-value="accountProfile"
      :is-reject-selection="false"
      class="select-profile-handle"
      @select-option="selectProfile"
    >
      <template #select-item="item">
        <img :src="getImg(item)" alt="User picture" class="user-picture" />
      </template>
    </BaseSearchField>

    <CommonCalendar width="408" position="top" class="date-picker" />

    <footer class="create-project__footer">
      <ButtonWithArrow
        :is-disabled="!projectName"
        class="button"
        @click="saveChanges"
      >
        <span>Save Project</span>
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapState, mapActions, createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseInput from '@/components/common/BaseInput'
import BaseSearchField from '@/components/BaseSearchField'
import AccountAnalysisSourcesTabs from '@/components/account-analysis/AccountAnalysisSourcesTabs'
import CommonCalendar from '@/components/datepicker/CommonCalendar'
import ButtonWithArrow from '@/components/common/ButtonWithArrow'

const {
  mapActions: mapAccountAnalysisActions,
  mapState: mapAccountAnalysisState,
} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'CreateAccountAnalysisProject',
  components: {
    BaseInput,
    AccountAnalysisSourcesTabs,
    CommonCalendar,
    ButtonWithArrow,
    BaseSearchField,
  },
  data() {
    return {
      projectName: '',
      accountProfile: '',
    }
  },
  computed: {
    ...mapState({
      additionalFilters: (state) => state.additionalFilters,
      userInfo: (state) => state.userInfo,
      newWorkspace: (state) => state.newAccountAnalysisWorkspace,
      newProject: (state) => state.newAccountAnalysisProject,
    }),
    ...mapAccountAnalysisState({
      listOfProfiles: (state) => state.listOfProfileHandle,
      newProjectId: (state) => state.newProjectId,
      newWorkspaceId: (state) => state.newWorkspaceId,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    profileNames() {
      return this.listOfProfiles.map((el) => el.user_alias)
    },
    defaultDateRange() {
      return [this.getLastWeeksDate(), new Date()]
    },
  },
  created() {
    this[action.GET_LIST_OF_PROFILE_HANDLE]()

    if (this.defaultDateRange.length) {
      this[action.UPDATE_ADDITIONAL_FILTERS]({
        date_range: this.defaultDateRange,
      })
    }
  },
  methods: {
    ...mapActions([
      action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    ...mapAccountAnalysisActions([
      action.GET_LIST_OF_PROFILE_HANDLE,
      action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE,
      action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT,
    ]),
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
    },
    async saveChanges() {
      await this[action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({
        title: this.projectName,
        profile_handle: this.accountProfile,
        source_filter: ['twitter'],
        members: [this.userInfo.id],
        creator: this.userInfo.id,
        start_search_date: this.additionalFilters.date_range[0],
        end_search_date: this.additionalFilters.date_range[1],
      })

      if (+this.workspaceId) {
        await this[action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({
          ...this.newProject,
          workspace: +this.workspaceId,
        })
      } else {
        await this[action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE]({
          ...this.newWorkspace,
          projects: [
            {
              ...this.newProject,
            },
          ],
        })
      }
      this.$router.push({
        name: 'AccountAnalysisDashboard',
        params: {
          projectId: this.newProjectId,
          workspaceId: this.newWorkspaceId || this.workspaceId,
        },
      })
    },
    selectProfile(name, searchValue) {
      this.accountProfile = searchValue
    },
    getImg(profileData) {
      return this.listOfProfiles.find(
        (profileOption) => profileData.item === profileOption.user_alias
      )?.user_picture
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

  .tabs {
    margin-bottom: 36px;
  }

  .input-name-field {
    max-width: 408px;
    margin-bottom: 32px;
  }

  .select-profile-handle {
    max-width: 408px;
    margin-bottom: 32px;

    .user-picture {
      width: 20px;
      height: 20px;
      margin-right: 10px;

      border-radius: 100%;
    }
  }

  .date-picker {
    max-width: 408px;
    margin-bottom: 72px;
  }

  .create-project__footer {
    display: flex;
    justify-content: flex-end;

    max-width: 408px;
  }
}
</style>
