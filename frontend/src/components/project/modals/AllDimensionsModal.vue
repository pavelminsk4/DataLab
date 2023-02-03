<template>
  <BaseModal
    v-if="authorsList"
    modal-frame-style="width: 40vw; max-height: 80vh;"
    title="Widgets Dimensions"
  >
    <div class="title">Author</div>

    <SelectWithCheckboxes
      v-model="author"
      name="author"
      :list="authorsList"
      placeholder="Search the author"
      :current-value="author"
      :is-search="true"
      :is-reject-selection="false"
      @update:modelValue="getResult"
      class="select"
    />

    <div class="title">Sentiment</div>

    <div class="sentiments">
      <BaseCheckbox
        v-for="(item, index) in sentiments"
        :key="item + index"
        :id="item"
        :has-icon="false"
        :model-value="isCheckedElement(item)"
        :class="['item', isCheckedElement(item) && `${item}-item`]"
        @change="onChange"
      >
        {{ capitalizeFirstLetter(item) }}
      </BaseCheckbox>
    </div>

    <BaseButton class="button" @click="saveChanges">Save</BaseButton>
  </BaseModal>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/buttons/BaseButton'
import BaseCheckbox from '@/components/BaseCheckbox'
import SelectWithCheckboxes from '@/components/SelectWithCheckboxes'

export default {
  name: 'AllDimensionsModal',
  components: {
    SelectWithCheckboxes,
    BaseCheckbox,
    BaseButton,
    BaseModal,
  },
  props: {
    projectId: {
      type: [String, Number],
      required: false,
    },
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      author: '',
      sentiments: ['neutral', 'negative', 'positive'],
      selectedSentiments: [],
    }
  },
  created() {
    this[action.GET_DIMENSION_AUTHORS](this.projectId)

    console.log(this.dimensionAuthors)
  },
  computed: {
    ...mapGetters({dimensionAuthors: get.DIMENSION_AUTHORS}),
    authorsList() {
      return this.dimensionAuthors?.map((el) => el.entry_author)
    },
    selectedSentimentsProxy: {
      get() {
        return (
          this.currentProject.sentiment_dimensions || this.selectedSentiments
        )
      },
      set(val) {
        this.selectedSentiments = val
      },
    },
  },
  methods: {
    ...mapActions([action.UPDATE_PROJECT, action.GET_DIMENSION_AUTHORS]),
    capitalizeFirstLetter,
    getResult(searchValue, name) {
      try {
        this[name] = searchValue
        this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: searchValue})

        switch (name) {
          case 'country':
            return this[action.GET_COUNTRIES](
              this.capitalizeFirstLetter(searchValue)
            )
          case 'author':
            return this[action.GET_AUTHORS](searchValue)
        }
      } catch (e) {
        console.log(e)
      }
    },
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.selectedSentimentsProxy.push(id)
      } else {
        let element = this.selectedSentimentsProxy.indexOf(id)
        this.removeSelectedFilter(element, id)
      }
    },
    removeSelectedFilter(index) {
      this.selectedSentimentsProxy.splice(index, 1)
    },
    isCheckedElement(item) {
      return this.selectedSentimentsProxy?.some((el) => el === item)
    },
    saveChanges() {
      try {
        this[action.UPDATE_PROJECT]({
          projectId: this.projectId,
          data: {
            sentiment_dimensions: this.selectedSentimentsProxy,
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
.title {
  margin-bottom: 4px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-title-color);
}

.select {
  margin-bottom: 20px;
}

.sentiments {
  display: flex;
  gap: 8px;

  .item {
    padding: 6px 12px;

    border: 1px solid var(--border-color);
    border-radius: 12px;

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-title-color);
  }

  .neutral-item {
    border: 1px solid var(--neutral-primary-color);

    color: var(--neutral-primary-color);
  }

  .negative-item {
    border: 1px solid var(--negative-primary-color);

    color: var(--negative-primary-color);
  }

  .positive-item {
    border: 1px solid var(--positive-primary-color);

    color: var(--positive-primary-color);
  }
}

.button {
  width: 59px;
  margin-top: 32px;
  margin-left: auto;
}
</style>
