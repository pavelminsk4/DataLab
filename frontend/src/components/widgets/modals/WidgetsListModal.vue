<template>
  <BaseModal title="Widgets">
    <div class="widgets-list-wrapper">
      <section class="widgets-wrapper">
        <BaseCheckbox
          v-for="(item, index) of widgetsNames"
          :key="index"
          :label="item.default_title"
          :id="item.id"
          :checked="item.is_active"
          @update:modelValue="updateWidgetsList($event, item.id)"
          class="checkbox"
        >
          <CustomText tag="span" :text="item.default_title" class="name" />
        </BaseCheckbox>

        <BaseButton class="button" @click="saveCollectionWidgets">
          <SaveIcon color="#ffffff" />
          <CustomText text="Save" />
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

import CustomText from '@components/CustomText'
import BaseModal from '@components/modals/BaseModal'
import BaseCheckbox from '@components/BaseCheckbox'
import BaseButton from '@components/common/BaseButton'
import WidgetsListIcon from '@components/icons/WidgetsListIcon'
import SaveIcon from '@components/icons/SaveIcon'

export default {
  name: 'WidgetsModal',
  components: {
    SaveIcon,
    WidgetsListIcon,
    BaseButton,
    BaseCheckbox,
    BaseModal,
    CustomText,
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
    widgetsNames() {
      if (this.widgets) {
        return Object.values(this.widgets).filter((el) => el.default_title)
      }

      return []
    },
  },
  methods: {
    updateWidgetsList(checked, id) {
      const widgetName = Object.keys(this.widgets).find(
        (widgetName) => this.widgets[widgetName].id === id
      )

      this.collection.push({name: widgetName, checked})
    },
    saveCollectionWidgets() {
      this.collection.forEach(({name, checked}) => {
        this.widgets[name].is_active = checked
      })

      this.$emit('update-available-widgets', {
        projectId: this.projectId,
        widgetsList: this.widgets,
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

      height: auto;

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
