<template>
  <section class="key-words-settings">
    <div class="mode-wrapper">
      <div class="mode-title mode-active">Simple mode</div>
    </div>

    <div class="second-title">Define the main keywords (OR)</div>
    <BaseTag
      name="keywords"
      :model-value="mainKeywords"
      :has-error="hasErrorMainField"
      error-message="Required field"
      :is-main-field="true"
      placeholder='Enter a main keyword and press "Enter"'
      @start-search="showResults"
      @update:modelValue="updateCollection"
    />

    <section class="additional-key-words">
      <div class="additional-key-block">
        <div class="second-title">
          Add Additional keywords <br />
          (And)
        </div>
        <BaseTag
          :model-value="additionalKeywords"
          :textarea="true"
          :is-additional-keywords="true"
          name="additional_keywords"
          placeholder="Enter additional keywords"
          class="additional-key"
          @update:modelValue="updateCollection"
        />
      </div>

      <div class="additional-key-block">
        <div class="second-title">
          Exclude Irrelevant keywords <br />
          (And Not)
        </div>
        <BaseTag
          :model-value="excludeKeywords"
          :is-irrelevant-keywords="true"
          class="additional-key"
          name="ignore_keywords"
          placeholder="Enter irrelevant keywords"
          @update:modelValue="updateCollection"
        />
      </div>
    </section>

    <div class="filters-title">Refine youre search with additional filters</div>

    <OnlineType :current-project="currentProject" />

    <BaseButton @click="showResults" class="apply-settings">
      Preview
    </BaseButton>
  </section>
</template>

<script>
import BaseTag from '@/components/BaseTag'
import OnlineType from '@/components/workspace/sources/OnlineType'
import BaseButton from '@/components/buttons/BaseButton'
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

export default {
  name: 'SimpleModeTab',
  components: {BaseButton, OnlineType, BaseTag},
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
  },
  data() {
    return {
      hasErrorMainField: false,
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

      if (!this.mainKeywords.length && name === 'keywords') {
        this.hasErrorMainField = true
      } else {
        this.hasErrorMainField = false
      }
    },
    showResults() {
      this.$emit('show-result')
    },
  },
}
</script>

<style lang="scss" scoped>
.key-words-settings {
  display: flex;
  flex-direction: column;

  width: 37vw;

  .mode-wrapper {
    display: flex;

    margin: 30px 0 20px 0;

    border-bottom: 1px solid var(--input-border-color);

    .mode-title {
      padding-bottom: 10px;

      font-size: 14px;
      color: rgba(255, 255, 255, 0.8);

      &:first-child {
        margin-right: 55px;
      }
    }

    .mode-active {
      border-bottom: 2px solid var(--button-primary-color);

      font-weight: 500;
      color: var(--primary-text-color);
    }
  }

  .second-title {
    margin-bottom: 12px;

    font-size: 14px;
    color: var(--primary-text-color);
  }

  .additional-key-words {
    display: flex;

    width: 100%;
    margin: 26px 0 40px;

    .additional-key-block {
      flex: 1;

      &:first-child {
        margin-right: 16px;
      }

      .additional-key {
        align-items: flex-start;
        flex-wrap: wrap;

        height: 110px;
      }
    }
  }
}

.filters-title {
  margin-bottom: 25px;

  font-weight: 600;
  font-size: 16px;
  color: var(--primary-text-color);
}

.apply-settings {
  align-self: flex-end;

  width: 100%;
}

@media screen and (max-width: 1180px) {
  .additional-key-words {
    flex-direction: column;

    .additional-key-block {
      width: 100%;

      margin: 0;

      &:first-child {
        margin-bottom: 20px;
      }
    }
  }
}
</style>
