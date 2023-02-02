<template>
  <div class="email-wrapper">
    <DivWithError
      :hasError="hasError"
      :errorMessage="errorMessage"
      class="email-field-error-wrapper"
    >
      <div :class="['email-field scroll', visible && 'active-email-field']">
        <div
          v-for="(item, index) in selectedUsers || []"
          :key="item"
          :class="['selected-user', 'duplicate' && isDuplicate]"
        >
          {{ item.email }}
          <DeleteTagButton @click="$emit('remove-user', index)" />
        </div>
        <div @click="addUsers" class="add-users-button">
          Add Users <AddButtonIcon />
        </div>
      </div>
    </DivWithError>

    <ul v-if="visible" class="select-list scroll">
      <li
        v-for="(item, index) in usersEmailsList"
        :key="item.username + index"
        class="select-item"
        @click="selectUser(item)"
      >
        {{ item.email }}
      </li>
    </ul>
  </div>
</template>

<script>
import AddButtonIcon from '@/components/icons/AddButtonIcon'
import DivWithError from '@/components/DivWithError.vue'
import DeleteTagButton from '@/components/icons/DeleteTagButton'

export default {
  name: 'AddUsersField',
  components: {
    AddButtonIcon,
    DivWithError,
    DeleteTagButton,
  },
  props: {
    hasError: {
      type: Boolean,
      default: false,
    },
    errorMessage: {
      type: String,
      default: '',
    },
    selectedUsers: {
      type: Array,
      default: () => [],
    },
    usersEmails: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      visible: false,
      isDuplicate: false,
    }
  },
  computed: {
    usersEmailsList() {
      return this.usersEmails.filter(
        (email) => !this.selectedUsers.includes(email)
      )
    },
  },
  created() {
    document.addEventListener('click', this.close)
  },
  unmounted() {
    document.removeEventListener('click', this.close)
  },
  methods: {
    addUsers() {
      this.visible = !this.visible
    },
    close({target}) {
      const selectList = document.querySelector('.email-wrapper')
      const isSelectInput =
        selectList.contains(target) || target.classList.contains('select-item')

      if (!isSelectInput) {
        this.visible = false
      }
    },
    selectUser(item) {
      const isSelectedUser = this.selectedUsers.find(
        (user) => user.id === item.id
      )
      if (isSelectedUser) {
        this.isDuplicate = true
      } else {
        this.$emit('select-user', item)
      }

      if (!this.usersEmailsList.length) {
        this.visible = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.email-wrapper {
  .email-field {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;

    height: auto;
    max-height: 110px;
    width: 516px;
    padding: 8px;

    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;

    overflow-x: auto;

    .selected-user {
      display: flex;
      align-items: center;
      gap: 6px;

      height: 25px;
      padding: 8px;

      border-radius: 8px;
      background-color: rgba(255, 255, 255, 0.2);

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--primary-text-color);
    }

    .duplicate {
      color: var(--primary-text-color);

      background: var(--negative-status);
      animation: shake 1s;
    }
    .add-users-button {
      display: flex;
      align-items: center;
      flex-shrink: 0;
      gap: 6px;

      height: 25px;
      padding: 8px;

      border-radius: 8px;
      background-color: rgba(145, 152, 167, 0.2);

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-secondary-color);

      &:hover {
        background-color: var(--button-primary-hover-color);
      }
    }
  }

  .active-email-field {
    outline: 1px solid var(--button-primary-color);
    border-radius: 10px 10px 0 0;
  }

  .select-list {
    position: absolute;
    z-index: 1;

    padding: 0;
    margin: 0;
    width: 516px;
    max-height: 250px;

    outline: 1px solid var(--button-primary-color);
    border-top: 1px solid var(--modal-line-color);
    box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
    border-radius: 0 0 10px 10px;
    background-color: var(--secondary-bg-color);

    font-size: 14px;
    list-style-type: none;
    overflow-y: auto;
    overflow-x: hidden;

    .select-item {
      padding: 10px;

      cursor: pointer;
      list-style-type: none;

      color: var(--primary-text-color);

      &:hover {
        background: var(--button-primary-color);
      }
    }
  }
}

.email-field-error-wrapper {
  width: fit-content;
  border-radius: 10px;
}
</style>
