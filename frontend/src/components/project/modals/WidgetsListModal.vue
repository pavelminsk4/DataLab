<template>
  <BaseModal title="Widgets">
    <div class="widgets-list-wrapper">
      <section class="widgets-wrapper">
        <BaseCheckbox
          v-for="(item, index) of widgetNames"
          :key="index"
          :label="item.default_title"
          :id="index"
          :model-value="item.is_active"
          @change="onChange"
          class="checkbox"
        >
          <span class="name">{{ item.default_title }}</span>
        </BaseCheckbox>

        <BaseButton class="button" @click="saveCollectionWidgets">
          <SaveIcon />
          Save
        </BaseButton>
      </section>
      <section class="icon-wrapper">
        <WidgetsListIcon />
      </section>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseButton from '@/components/common/BaseButton'
import WidgetsListIcon from '@/components/icons/WidgetsListIcon'
import SaveIcon from '@/components/icons/SaveIcon'

export default {
  name: 'WidgetsModal',
  components: {
    SaveIcon,
    WidgetsListIcon,
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
        return availableWidgets.filter((el) => el.default_title)
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
        ...widgetsKeys.map((el) => ({
          [el]: {is_active: false, id: this.widgets[el].id},
        }))
      )
      const activeWidgets = Object.assign(
        {},
        ...this.collectionProxy.map((el) => ({
          [el]: {is_active: true, id: this.widgets[el].id},
        }))
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
        this.collectionProxy.filter((i, index) => {
          if (i === item) {
            this.removeSelectedFilter(index)
          }
        })
      }
    },
    async saveCollectionWidgets() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: this.availableCollection,
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-list-wrapper {
  display: flex;

  margin: -24px;

  .widgets-wrapper {
    display: flex;
    flex-direction: column;
    gap: 12px;

    padding: 24px 32px;

    .checkbox {
      gap: 10px;
      padding: 14px;

      border-radius: 10px;
      border: 1px solid var(--border-color);

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-title-color);
    }

    .active-element {
      border: 1px solid var(--border-active-color);
      background-color: var(--primary-active-color);
    }

    .button {
      display: flex;
      gap: 10px;
      align-self: flex-end;

      margin-top: 40px;
    }
  }

  .icon-wrapper {
    padding: 36px 34px 0;

    background-color: var(--background-primary-color);
  }
}
</style>
