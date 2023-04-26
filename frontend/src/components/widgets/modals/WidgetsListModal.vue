<template>
  <BaseModal title="Widgets">
    <div class="widgets-list-wrapper">
      <section class="widgets-wrapper">
        <BaseCheckbox
          v-for="(item, index) of widgetNames"
          :key="index"
          :label="item.default_title"
          :id="item.id"
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
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

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
    projectId: {type: Number, required: true},
    widgetList: {type: Object, default: null},
  },
  data() {
    return {
      collection: [],
    }
  },
  computed: {
    ...mapGetters({availableWidgets: get.AVAILABLE_WIDGETS}),
    widgets() {
      return this.widgetList || this.availableWidgets
    },
    widgetNames() {
      if (this.widgets) {
        return Object.values(this.widgets).filter((el) => el.default_title)
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
          [el]: {...this.widgets[el], is_active: false},
        }))
      )
      const activeWidgets = Object.assign(
        {},
        ...this.collectionProxy.map((el) => ({
          [el]: {...this.widgets[el], is_active: true},
        }))
      )
      return {...notActiveWidgets, ...activeWidgets}
    },
  },
  methods: {
    removeSelectedFilter(index) {
      this.collectionProxy.splice(index, 1)
    },
    onChange({id, checked}) {
      const item = Object.keys(this.widgets).find(
        (widgetName) => this.widgets[widgetName].id === id
      )

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
    saveCollectionWidgets() {
      this.$emit('update-available-widgets', {
        projectId: this.projectId,
        widgetsList: this.availableCollection,
      })
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
