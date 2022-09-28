<template>
  <StepsNav
    v-if="this.currentStep === 'Step3'"
    :step="step"
    :title="'Define the search'"
    :hint="'Search by keywords and phrases'"
    :button-name="'Create Project'"
    @next-step="createWorkspaceAndProject"
  />

  <StepsNav
    v-else
    :step="step"
    :title="'Define the search'"
    :hint="'Search by keywords and phrases'"
    :is-existing-workspace="true"
    :button-name="'Create Project'"
    @next-step="createProject"
  />

  <div class="search-settings-wrapper">
    <section class="key-words-settings">
      <div class="mode-wrapper">
        <div class="mode-title mode-active">Simple mode</div>
        <div class="mode-title">Expert mode</div>
      </div>

      <div class="second-title">Define the main keywords (OR)</div>
      <BaseTag v-model="mainTags" :is-main-field="true" />

      <section class="additional-key-words">
        <div class="additional-key-block">
          <div class="second-title">
            Add Additional keywords <br />
            (And)
          </div>
          <BaseTag
            v-model="additionalTags"
            :textarea="true"
            :is-additional-keywords="true"
            class="additional-key"
          />
        </div>

        <div class="additional-key-block">
          <div class="second-title">
            Exclude Irrelevant keywords <br />
            (And Not)
          </div>
          <BaseTag
            v-model="excludeTags"
            :is-irrelevant-keywords="true"
            class="additional-key"
            :placeholder="'Enter Keywords and Phrases'"
          />
        </div>
      </section>

      <div class="filters-title">
        Refine youre search with additional filters
      </div>

      <OnlineType class="key-word-section" />

      <BaseButton @click="showResults" class="apply-settings">
        Apply Settings
      </BaseButton>
    </section>

    <SearchResults />
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'

import BaseTag from '@/components/BaseTag'
import StepsNav from '@/components/navigation/StepsNav'

import OnlineType from '@/components/workspace/sources/OnlineType'
import SearchResults from '@/components/SearchResults'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'CreateProjectSecondStep',
  components: {
    BaseButton,
    SearchResults,
    StepsNav,
    BaseTag,
    OnlineType,
  },
  data() {
    return {
      mainTags: [],
      additionalTags: [],
      excludeTags: [],
    }
  },
  computed: {
    ...mapState(['newWorkspace', 'newProject', 'currentStep']),
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
    }),
    step() {
      return this.$route.name
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_PROJECT_STATE,
      action.UPDATE_NEW_WORKSPACE,
      action.CREATE_WORKSPACE,
      action.CREATE_PROJECT,
      action.GET_WORKSPACES,
      action.POST_SEARCH,
      action.CLEAR_STATE,
    ]),
    showResults() {
      try {
        this[action.POST_SEARCH]({
          keywords: this.mainTags,
          additions: this.additionalTags,
          exceptions: this.excludeTags,
          ...this.additionalFilters,
        })
      } catch (e) {
        console.log(e)
      }
    },

    createWorkspaceAndProject() {
      try {
        this[action.UPDATE_PROJECT_STATE]({
          keywords: [...this.mainTags],
          additional_keywords: [...this.additionalTags],
          ignore_keywords: [...this.additionalTags],
        })
        this[action.UPDATE_NEW_WORKSPACE]({
          projects: [this.newProject],
        })
        this[action.CREATE_WORKSPACE](this.newWorkspace)
        this[action.CLEAR_STATE]()
        this[action.GET_WORKSPACES]()
        this.$router.push({
          name: 'Home',
        })
        this[action.GET_WORKSPACES]()
      } catch (e) {
        console.log(e)
      }
    },
    createProject() {
      try {
        this[action.UPDATE_PROJECT_STATE]({
          keywords: [...this.mainTags],
          additional_keywords: [...this.additionalTags],
          ignore_keywords: [...this.additionalTags],
        })
        this[action.CREATE_PROJECT](this.newProject)
        this[action.CLEAR_STATE]()
        this[action.GET_WORKSPACES]()
        this.$router.push({
          name: 'Workspace',
          params: {
            workspaceId: this.$route.params.workspaceId,
          },
        })
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.mode-wrapper {
  display: flex;

  margin: 30px 0 20px 0;

  border-bottom: 1px solid var(--input-border-color);
}

.mode-title {
  padding-bottom: 10px;

  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);

  &:first-child {
    margin-right: 55px;
  }
}

.mode-active {
  border-bottom: 2px solid var(--primary-button-color);

  font-weight: 500;
  color: var(--primary-text-color);
}

.search-settings-wrapper {
  display: flex;
  justify-content: space-between;
}

.second-title {
  margin-bottom: 12px;

  font-size: 14px;
  color: var(--primary-text-color);
}

.filters-wrapper {
  display: flex;
  justify-content: space-between;
}

.additional-key-words {
  display: flex;

  width: 100%;
  margin: 26px 0 40px;
}

.additional-key-block {
  flex: 1;

  &:first-child {
    margin-right: 16px;
  }
}

.additional-key {
  align-items: flex-start;
  flex-wrap: wrap;

  height: 110px;

  padding-top: 10px;
}

.filters-title {
  margin-bottom: 25px;

  font-weight: 600;
  font-size: 16px;
  color: var(--primary-text-color);
}

.key-words-settings {
  display: flex;
  flex-direction: column;

  width: 50%;
}

.apply-settings {
  align-self: flex-end;
}

.radio-btn {
  display: flex;

  margin-right: 25px;

  color: var(--primary-text-color);

  cursor: pointer;
}

.not-check {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 20px;
  height: 20px;
  margin-right: 7px;

  border: 1px solid var(--secondary-text-color);
  border-radius: 50px;

  cursor: pointer;
}

.radio-wrapper {
  display: flex;
  justify-content: space-between;

  margin: 10px 0 25px;
}

.back-button {
  cursor: pointer;

  color: var(--secondary-text-color);
}

.arrow-back {
  margin-right: 6px;
}

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--primary-text-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.next-button {
  width: 114px;
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}

.key-word-section {
  width: 515px;
  margin-top: 30px;
}

@media screen and (max-width: 1180px) {
  .additional-key-words {
    flex-direction: column;

    .additional-key-block {
      margin: 0;

      &:first-child {
        margin-bottom: 20px;
      }
    }
  }
}
</style>
