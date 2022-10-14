<template>
  <BaseModal>
    <section>
      <div class="title">Widgets</div>
      <BaseCheckbox
        v-for="(item, index) of typesOfWidgets"
        :key="index"
        :label="item.name"
        :id="index"
        @change="onChange"
        >{{ item.name }}</BaseCheckbox
      >
    </section>
  </BaseModal>
</template>

<script>
import BaseModal from '@components/modals/BaseModal'
import BaseCheckbox from '@/components/BaseCheckbox'

export default {
  name: 'WidgetsModal',
  components: {
    BaseCheckbox,
    BaseModal,
  },
  data() {
    return {
      collection: [],
    }
  },
  computed: {
    typesOfWidgets() {
      return [{name: 'Summary'}, {name: 'Content Volume'}]
    },
  },
  methods: {
    removeSelectedFilter(index) {
      this.collection.splice(index, 1)
    },
    onChange(args) {
      const {id, checked} = args
      const item = this.typesOfWidgets[id].name
      if (checked) {
        if (this.collection.indexOf(item) < 0) {
          this.collection.push(item)
        }
      } else {
        this.collection = this.collection.filter((i) => i !== item)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
  color: var(--primary-text-color);
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
