FILES_MAIN	=	main_thibault.c				\
				template_list.c				\
				core_template.c				\
				core_node.c					\
				char_node.c					\
				core_score.c				\
				linked_list_node.c			\
				core_char.c					\
				core.c

FILES_TEST	=	testeur_thibault.c			\
				template_list.c				\
				core_template.c				\
				core_node.c					\
				char_node.c					\
				core_score.c				\
				linked_list_node.c			\
				core_char.c					\
				core.c



S_PATH	=	srcs/
O_PATH	=	objs/
I_PATH	=	includes/

SRCS_MAIN	=	${addprefix ${S_PATH}, ${FILES_MAIN}}
OBJS_MAIN	=	${addprefix ${O_PATH}, ${FILES_MAIN:.c=.o}}

SRCS_TEST	=	${addprefix ${S_PATH}, ${FILES_TEST}}
OBJS_TEST	=	${addprefix ${O_PATH}, ${FILES_TEST:.c=.o}}

BINARIES	=	Solver	\
				Test

CC		=	clang

RM		=	rm -rf

CFLAGS	=	-Wall -Wextra -Werror -pedantic -O0 -g3 -fsanitize=address -fno-omit-frame-pointer -fno-optimize-sibling-calls

${O_PATH}%.o:	${S_PATH}%.c
				@mkdir -p ${dir $@}
				@${CC} ${CFLAGS} -c $< -o $@ -I @{I_PATH}
				@echo "${BOLD}${CYAN}Compiling${S}${S} ${IGREY}$<${S} ${YELLOW}-> ${S}${SBLUE}$@${S} ⚙️"


Solver:		${OBJS_MAIN}
			@${CC} ${OBJS_MAIN} ${CFLAGS} -o $@ -lreadline -I ${I_PATH}
			@echo ""
			@echo "${BOLD}${PURPLE}Building${S}${S} ${IGREY}$@${S} 🖥️"
			@echo ""
			@echo "\033[3;92mCompilation is completed !${S} 🎉"

Test:		${OBJS_TEST}
			@${CC} ${OBJS_TEST} ${CFLAGS} -o $@ -lreadline -I ${I_PATH}
			@echo ""
			@echo "${BOLD}${PURPLE}Building${S}${S} ${IGREY}$@${S} 🖥️"
			@echo ""
			@echo "\033[3;92mCompilation is completed !${S} 🎉"

all:		Solver Test

clean:
			@${RM} ${O_PATH}
			@echo "${BOLD}${SRED}Removing${S}${S} ${IGREY}${O_PATH}${S} 🗑️"

fclean:		clean
			@${RM} ${BINARY}
			@echo "${BOLD}${SRED}Removing${S}${S} ${IGREY}${NAME}${S} 🗑️"

space:
			@echo " "

re:			fclean space all

test:		re
			@echo ""
			@echo "${BOLD}${PURPLE}Launching tests${S}${S} 🖥️"
			@echo ""
			@./Test

.PHONY: all clean fclean re bonus

S 		=		\033[0m
BOLD 	= 		\033[1m
ITALIC 	= 		\033[3m
UNDER 	= 		\033[4m
REV 	= 		\033[7m

# Colors
GREY 	= 		\033[30m
RED 	= 		\033[31m
GREEN	=		\033[32m
YELLOW	=		\033[33m
BLUE	=		\033[34m
PURPLE	=		\033[35m
CYAN	=		\033[36m
WHITE	=		\033[37m

SGREY	=		\033[90m
SRED	=		\033[91m
SGREEN	=		\033[92m
SYELLOW	=		\033[93m
SBLUE	=		\033[94m
SPURPLE	=		\033[95m
SCYAN	=		\033[96m
SWHITE	=		\033[97m

# Colored backgrounds

IGREY	=		\033[40m
IRED	=		\033[41m
IGREEN	=		\033[42m
IYELLOW	=		\033[43m
IBLUE	=		\033[44m
IPURPLE	=		\033[45m
ICYAN	=		\033[46m
IWHITE	=		\033[47m