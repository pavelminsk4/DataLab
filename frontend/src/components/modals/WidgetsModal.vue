<template>
  <BaseModal>
    <section class="widgets-wrapper">
      <div class="title">Widgets</div>
      <BaseCheckbox
        v-for="(item, index) of widgetNames"
        :key="index"
        :label="item.name"
        :id="index"
        :model-value="item.is_active"
        @change="onChange"
      >
        {{ item.name }}
      </BaseCheckbox>

      <BaseButton class="button" @click="saveCollectionWidgets">
        Save
      </BaseButton>
    </section>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@components/modals/BaseModal'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'WidgetsModal',
  components: {
    BaseButton,
    BaseCheckbox,
    BaseModal,
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      collection: [],
    }
  },
  created() {
    this[action.GET_AVAILABLE_WIDGETS](this.projectId)
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS}),
    widgetNames() {
      if (this.widgets) {
        const availableWidgets = Object.values(this.widgets)
        return availableWidgets.filter((el) => el.name)
      }

      return []
    },
    collectionProxy: {
      get() {
        let collection = []
        for (let key in this.widgets) {
          if (this.widgets[key].is_active) {
            collection.push(key)
          }
        }
        return collection || []
      },
      set(val) {
        this.collection = val
      },
    },
    availableCollection() {
      const widgetsKeys = Object.keys(this.widgets)
      const notActiveWidgets = Object.assign(
        {},
        ...widgetsKeys.map((el) => ({[el]: false}))
      )
      const activeWidgets = Object.assign(
        {},
        ...this.collectionProxy.map((el) => ({[el]: true}))
      )
      return {...notActiveWidgets, ...activeWidgets}
    },
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
    removeSelectedFilter(index) {
      this.collectionProxy.splice(index, 1)
    },
    onChange(args) {
      const {id, checked} = args
      const item = Object.keys(this.widgets)[id]
      if (checked) {
        if (this.collectionProxy.indexOf(item) < 0) {
          this.collectionProxy.push(item)
        }
      } else {
        this.collectionProxy = this.collectionProxy.filter((i, index) =>
          this.removeSelectedFilter(index)
        )
      }
    },
    async saveCollectionWidgets() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: this.availableCollection,
      })
      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  display: flex;
  flex-direction: column;

  width: 47vw;
}

.title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
  color: var(--primary-text-color);
}

.button {
  align-self: flex-end;

  width: 103px;
}

.settings-options {
  display: flex;

  border-bottom: 1px solid var(--input-border-color);

  .option {
    cursor: pointer;

    padding-bottom: 12px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
    color: rgba(255, 255, 255, 0.8);

    &:first-child {
      margin-right: 25px;
    }
  }

  .option-active {
    border-bottom: 1px solid var(--primary-button-color);

    color: var(--primary-text-color);
  }
}

.form-sections {
  display: flex;
  flex-direction: column;

  margin-top: 25px;

  .form-title {
    margin-bottom: 12px;

    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 110%;
    color: var(--primary-text-color);
  }

  .input-settings {
    margin-bottom: 24px;
  }

  .description-field {
    width: 100%;
    height: 105px;
    padding: 10px 19px;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    color: var(--primary-text-color);

    resize: none;
  }

  .description-field::placeholder {
    color: var(--secondary-text-color);
  }

  .description-field::-webkit-scrollbar {
    width: 10px;
  }

  .description-field::-webkit-scrollbar-track {
    border-radius: 10px;

    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  }

  .description-field::-webkit-scrollbar-thumb {
    width: 8px;

    border-radius: 10px;

    background-color: var(--box-shadow-color);
    outline: none;
  }

  .button {
    align-self: flex-end;

    margin-top: 20px;
    width: 103px;
  }
}
</style>
