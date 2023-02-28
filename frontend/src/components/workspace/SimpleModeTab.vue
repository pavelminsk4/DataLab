<template>
  <section class="key-words-settings">
    <div class="settings-wrapper">
      <div class="second-title">Define the main keywords (OR)</div>
      <BaseTag
        name="keywords"
        :model-value="mainKeywords"
        :has-error="!!mainKeywordsError"
        :error-message="mainKeywordsError"
        :is-main-field="true"
        placeholder='Enter a main keyword and press "Enter"'
        @update:modelValue="updateCollection"
      />

      <div class="second-title">Add Additional keywords (And)</div>
      <BaseTag
        :model-value="additionalKeywords"
        :textarea="true"
        :is-additional-keywords="true"
        name="additional_keywords"
        placeholder="Enter additional keywords"
        @update:modelValue="updateCollection"
      />

      <div class="second-title">Exclude Irrelevant keywords (And Not)</div>
      <BaseTag
        :model-value="excludeKeywords"
        :is-irrelevant-keywords="true"
        name="ignore_keywords"
        placeholder="Enter irrelevant keywords"
        @update:modelValue="updateCollection"
      />

      <div class="filters-title">
        Refine youre search with additional filters
      </div>

      <OnlineType :current-project="currentProject" />
    </div>

    <div class="buttons">
      <BaseButton
        :is-not-background="true"
        class="apply-settings"
        @click="showResults"
      >
        Preview
      </BaseButton>

      <BaseButton :is-disabled="isDisabledButton" @click="saveProject">
        <SaveIcon class="save-icon" /> Save Project
      </BaseButton>
    </div>
  </section>
</template>

<script>
import BaseTag from '@/components/BaseTag'
import OnlineType from '@/components/workspace/sources/OnlineType'
import BaseButton from '@/components/common/BaseButton'
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import SaveIcon from '@/components/icons/SaveIcon'

export default {
  name: 'SimpleModeTab',
  components: {SaveIcon, BaseButton, OnlineType, BaseTag},
  props: {
    mainKeywords: {
      type: Array,
      default: () => [],
    },
    additionalKeywords: {
      type: Array,
      default: () => [],
    },
    excludeKeywords: {
      type: Array,
      default: () => [],
    },
    currentProject: {
      type: [Array, Object],
      default: () => [],
    },
    isDisabledButton: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      mainKeywordsError: null,
    }
  },
  computed: {
    ...mapGetters({
      searchData: get.SEARCH_DATA,
    }),
  },
  methods: {
    updateCollection(name, value) {
      this.$emit('update-collection', name, value)

      if (this.mainKeywords.length && name === 'keywords') {
        this.mainKeywordsError = null
      }
    },
    showResults() {
      if (!this.validation()) return

      this.$emit('show-result')
    },
    saveProject() {
      if (!this.validation()) return

      this.$emit('save-project')
    },
    validation() {
      if (!this.mainKeywords.length) {
        this.mainKeywordsError = 'required'
      }
      return !this.mainKeywordsError
    },
  },
}
</script>

<style lang="scss" scoped>
.key-words-settings {
  display: flex;
  flex-direction: column;

  width: 100%;
  margin: 20px 0 0 -24px;

  .settings-wrapper {
    padding: 0 40px 0 24px;
  }

  .second-title {
    margin: 20px 0 4px;

    font-size: 14px;
    color: var(--typography-primary-color);
  }
}

.filters-title {
  margin: 40px 0 20px;

  font-weight: 600;
  font-size: 16px;
  color: var(--typography-primary-color);
}

.buttons {
  position: -webkit-sticky;
  position: sticky;
  bottom: -24px;

  display: flex;
  justify-content: flex-end;
  gap: 16px;

  width: 100%;
  padding: 16px;

  border-top: var(--border-primary);
  background-color: var(--background-primary-color);

  .apply-settings {
    width: 80px;
  }

  .save-icon {
    margin-right: 5px;
  }
}
</style>
